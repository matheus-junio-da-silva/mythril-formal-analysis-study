import json
import z3 as z3_solver

from mythril.a_my_funcntions.store_rescue_constraints import retrieve_constraints


def generate_json_constraints(constraints, annotation, 
                              minimize=(), maximize=(), generate=False):
    """
    save constraints in a json file

    :param constraints: list of constraints
    :param minimize: Tuple of minimization conditions
    :param maximize: Tuple of maximization conditions
    :param generate: Boolean to generate the file
    :return:

    mythril/support/model.py
    """
    if generate:
        # Gerando IDs numéricos
        """constraints_json = [{"id": i+1, 
                             "expr": str(constraint).replace("\n", "")} for i, constraint in enumerate(constraints)]
                             """
        path_json = "mythril/a_my_funcntions/constraints.json"
        constraints_json = retrieve_constraints(annotation, path_json)

        minimize_json = [{"id": i+1, 
                          "expr": str(e).replace("\n", "")} for i, e in enumerate(minimize)]
        maximize_json = [{"id": i+1, 
                          "expr": str(e).replace("\n", "")} for i, e in enumerate(maximize)]
        
        # Criando dicionário para JSON
        data = {
            "total_constraints": len(constraints),
            "constraints": constraints_json,
            "minimize": minimize_json,
            "maximize": maximize_json,
        }
        
        json_path_save = "mythril/a_my_funcntions/z3_constraints.json"
        # Convertendo para JSON e salvando em arquivo
        with open(json_path_save, "w") as f:
            json.dump(data, f, indent=4)

def process_smt_lib(s, generate_files):
    """
    Process the SMT-LIB file, generate a file with the constraints 
    and run the solver
    
    :param s: Z3 solver with constraints loaded
    :param generate_files: Boolean to generate the file
    :return:
    
    mythril/support/model.py
    """

    if not generate_files:
        return
    
    try:
        smt_path = "mythril/a_my_funcntions/z3_constraints.smt2"

        # Salvar o estado SMT-LIB em um arquivo
        with open(smt_path, "w") as f:
            f.write(s.sexpr())
        
        with open(smt_path, "r") as f:
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

