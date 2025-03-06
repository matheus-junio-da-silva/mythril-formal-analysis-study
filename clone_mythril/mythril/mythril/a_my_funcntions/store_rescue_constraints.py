import json
"""
def store_constraints(constraints, pc, opcode, origin, creation_phase, json_path="constraints.json"):
    
    data = {
        "pc": pc,
        "opcode": opcode,
        "origin": origin,
        "creation_phase": creation_phase,
        "constraints": [str(c) for c in constraints]  # Convertendo constraints para string para armazenar
    }
    
    try:
        with open(json_path, "r") as file:
            stored_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        stored_data = []
    
    stored_data.append(data)
    
    with open(json_path, "w") as file:
        json.dump(stored_data, file, indent=4)"""

def store_constraints(pc, constraints, json_path="mythril/a_my_funcntions/constraints.json"):
    
    if not isinstance(constraints, list):
        constraints = [constraints]  # Garante que constraints seja sempre uma lista

    data = {
        "pc": pc,
        "constraints": [str(c) for c in constraints]  # Convertendo constraints para string para armazenar
    }
    
    try:
        with open(json_path, "r") as file:
            stored_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        stored_data = []
    
    stored_data.append(data)
    
    with open(json_path, "w") as file:
        json.dump(stored_data, file, indent=4)

def retrieve_constraints(annotation, json_path="mythril/a_my_funcntions/constraints.json"):
    """
    Recupera constraints com base nos endereços de instrução armazenados nas annotations.
    """
    try:
        with open(json_path, "r") as file:
            stored_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
    relevant_constraints = []
    
    for entry in stored_data:
        #if entry["pc"] in annotation.trace or entry["pc"] in annotation.path:
        if entry["pc"] in annotation.trace:
            relevant_constraints.append(entry)
    
    return relevant_constraints
