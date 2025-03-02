def generate_json_constraints(constraints, minimize, maximize, generate=False):
    """
    save constraints in a json file
    
    :param constraints: Tuple of constraints
    :param minimize: Tuple of minimization conditions
    :param maximize: Tuple of maximization conditions
    :param generate: Boolean to generate the file
    :return:

    mythril/support/model.py
    """
    if generate:
        # Gerando IDs numéricos
        constraints_json = [{"id": i+1, "expr": str(constraint).replace("\n", "")} for i, constraint in enumerate(constraints)]
        minimize_json = [{"id": i+1, "expr": str(e).replace("\n", "")} for i, e in enumerate(minimize)]
        maximize_json = [{"id": i+1, "expr": str(e).replace("\n", "")} for i, e in enumerate(maximize)]
        
        # Criando dicionário para JSON
        data = {
            "constraints": constraints_json,
            "minimize": minimize_json,
            "maximize": maximize_json,
        }
        
        # Convertendo para JSON e salvando em arquivo
        with open("z3_constraints.json", "w") as f:
            json.dump(data, f, indent=4)