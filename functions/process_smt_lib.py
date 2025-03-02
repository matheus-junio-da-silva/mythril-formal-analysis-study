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
