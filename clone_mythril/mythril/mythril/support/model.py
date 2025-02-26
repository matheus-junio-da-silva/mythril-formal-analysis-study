import logging
import os
import sys
from functools import lru_cache
from multiprocessing import TimeoutError
from multiprocessing.pool import ThreadPool
from pathlib import Path

from z3 import sat, unknown

from mythril.exceptions import SolverTimeOutException, UnsatError
from mythril.laser.ethereum.time_handler import time_handler
from mythril.laser.smt import And, Optimize, simplify
from mythril.support.support_args import args
from mythril.support.support_utils import ModelCache

import json
import z3 as z3_solver



log = logging.getLogger(__name__)


model_cache = ModelCache()


def solver_worker(
    constraints,
    minimize=(),
    maximize=(),
    solver_timeout=None,
):
    """
    Returns a model based on given constraints as a tuple
    :param constraints: Tuple of constraints
    :param minimize: Tuple of minimization conditions
    :param maximize: Tuple of maximization conditions
    :param solver_timeout: The timeout for solver
    :return:
    """
    s = Optimize()
    s.set_timeout(solver_timeout)

    for constraint in constraints:
        s.add(constraint)
    for e in minimize:
        s.minimize(e)
    for e in maximize:
        s.maximize(e)


    minhacondicao_debug = True
    if minhacondicao_debug:
        """
        # Gerando representação das constraints
        constraints_json = [str(constraint).replace("\n", "") for constraint in constraints]
        minimize_json = [str(e).replace("\n", "") for e in minimize]
        maximize_json = [str(e).replace("\n", "") for e in maximize]
        """

        """# Gerando IDs e representação das constraints
        constraints_json = [{"id": f"c{i+1}", "expr": str(constraint).replace("\n", "")} for i, constraint in enumerate(constraints)]
        minimize_json = [{"id": f"m{i+1}", "expr": str(e).replace("\n", "")} for i, e in enumerate(minimize)]
        maximize_json = [{"id": f"x{i+1}", "expr": str(e).replace("\n", "")} for i, e in enumerate(maximize)]
        """

        # Gerando IDs numéricos
        constraints_json = [{"id": i+1, "expr": str(constraint).replace("\n", "")} for i, constraint in enumerate(constraints)]
        minimize_json = [{"id": i+1, "expr": str(e).replace("\n", "")} for i, e in enumerate(minimize)]
        maximize_json = [{"id": i+1, "expr": str(e).replace("\n", "")} for i, e in enumerate(maximize)]
        
        
        # Gerando representação do solver (formato SMT-LIB)
        #solver_state = s.to_smt2()
        
        # Criando dicionário para JSON
        data = {
            "constraints": constraints_json,
            "minimize": minimize_json,
            "maximize": maximize_json,
            #"solver_state": solver_state
        }
        
        # Convertendo para JSON
        json_output = json.dumps(data, indent=4)
        with open("z3_constraints.json", "w") as f:
            json.dump(data, f, indent=4)
        #print(json_output)

        """
        try: 
            # Salvando as constraints em um arquivo binário
            with open("z3_constraints.pkl", "wb") as f:
                pickle.dump((constraints, minimize, maximize), f)
        except Exception as e:
            print(f"Erro ao salvar o arquivo: {e}")

        """

        """# Geração do JSON com melhorias
        constraints_json2 = [constraint.sexpr() if hasattr(constraint, "sexpr") else str(constraint) for constraint in constraints if constraint is not True]
        minimize_json2 = [e.sexpr() if hasattr(e, "sexpr") else str(e) for e in minimize]
        maximize_json2 = [e.sexpr() if hasattr(e, "sexpr") else str(e) for e in maximize]
        
        #solver_state = s.to_smt2()

        data2 = {
            "constraints(S-expressions)": constraints_json2,
            "minimize(S-expressions)": minimize_json2,
            "maximize(S-expressions)": maximize_json2,
            #"solver_state": solver_state
        }
        
        json_output2 = json.dumps(data2, indent=4)
        print(json_output2)"""

    if args.solver_log:
        Path(args.solver_log).mkdir(parents=True, exist_ok=True)
        constraint_hash_input = tuple(
            list(constraints)
            + list(minimize)
            + list(maximize)
            + [len(constraints), len(minimize), len(maximize)]
        )
        with open(
            args.solver_log + f"/{abs(hash(constraint_hash_input))}.smt2", "w"
        ) as f:
            f.write(s.sexpr())

    if minhacondicao_debug:
        try:
            # Salvar o estado SMT-LIB em um arquivo
            with open("z3_constraints.smt2", "w") as f:
                f.write(s.sexpr())

            with open("z3_constraints.smt2", "r") as f:
                smt2_constraints = f.read()
            s_new = z3_solver.Optimize()
            # Carregar as restrições para o solver
            s_new.from_string(smt2_constraints)

            # Rodar o solver
            result = s_new.check()

            # Verificar resultado
            if result == z3_solver.sat:
                print("Satisfiável! Modelo:")
                print(s_new.model())
            elif result == z3_solver.unsat:
                print("Insatisfiável!")
            else:
                print("Resultado desconhecido.")    
        except Exception as e:
            print(f"Erro ao salvar o arquivo: {e}")


    result = s.check()
    return result, s


@lru_cache(maxsize=2**23)
def get_model(
    constraints,
    minimize=(),
    maximize=(),
    solver_timeout=None,
):
    """
    Returns a model based on given constraints as a tuple
    :param constraints: Tuple of constraints
    :param minimize: Tuple of minimization conditions
    :param maximize: Tuple of maximization conditions
    :param solver_timeout: The solver timeout
    :return:
    """

    solver_timeout = solver_timeout or args.solver_timeout
    solver_timeout = min(solver_timeout, time_handler.time_remaining())
    if solver_timeout <= 0:
        raise SolverTimeOutException
    for constraint in constraints:
        if isinstance(constraint, bool) and not constraint:
            raise UnsatError

    if isinstance(constraints, tuple) is False:
        constraints = constraints.get_all_constraints()
    constraints = [
        constraint
        for constraint in constraints
        if isinstance(constraint, bool) is False
    ]

    if len(maximize) + len(minimize) == 0:
        ret_model = model_cache.check_quick_sat(simplify(And(*constraints)).raw)
        if ret_model:
            return ret_model
    pool = ThreadPool(1)
    try:
        thread_result = pool.apply_async(
            solver_worker, args=(constraints, minimize, maximize, solver_timeout)
        )
        try:
            result, s = thread_result.get(solver_timeout)
        except TimeoutError:
            result = unknown
        except Exception:
            log.warning("Encountered an exception while solving expression using z3")
            result = unknown
    finally:
        # This is to prevent any segmentation faults from being displayed from z3
        sys.stdout = open(os.devnull, "w")
        sys.stderr = open(os.devnull, "w")
        pool.terminate()
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    if result == sat:
        model_cache.model_cache.put(s.model(), 1)
        print("(original) satisfiável!")
        return s.model()
    elif result == unknown:
        print("(original) nao satisfiável!")
        log.debug("Timeout/Error encountered while solving expression using z3")
        raise SolverTimeOutException
    raise UnsatError
