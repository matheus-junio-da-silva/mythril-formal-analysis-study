import json
import sys
from mythril.a_my_funcntions.generate_final_json_and_smt import generate_json_constraints

def load_json(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_json(filepath, data):
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Erro ao salvar JSON: {e}")
        sys.exit(1)

def validate_address(json_data):
    if 'address_instruction_required' not in json_data:
        print("Erro: 'address_instruction_required' não encontrado no JSON.")
        sys.exit(1)
    return json_data['address_instruction_required']

def check_and_add_path(json_data, path, path_key, address_instruction_required, global_state):
    if global_state.instruction['address'] == address_instruction_required:
        if path_key not in json_data:
            json_data[path_key] = path
            save_json('mythril/a_my_funcntions/temp_data.json', json_data)
            sys.exit(1)

def process_json_validation(global_state):
    try:
        json_data = load_json('mythril/a_my_funcntions/temp_data.json')
        address_instruction_required = validate_address(json_data)
        
        check_and_add_path(json_data, global_state._annotations[0].trace, 'path', address_instruction_required, global_state)
        check_and_add_path(json_data, global_state._annotations[1].path, 'path2', address_instruction_required, global_state)    
        return True
    except Exception as e:
        print(f"Erro inesperado: {e}")
        sys.exit(1)

def json_validation_and_generation(global_state, constraints, minimize=(), maximize=()):
    """Executa a validação do JSON e gera as restrições apenas se a validação for bem-sucedida."""
    try:
        if process_json_validation(global_state):
            generate_json_constraints(
                constraints, global_state._annotations[0], minimize, maximize, generate=True
            )
    except Exception as e:
        print(f"Erro inesperado: {e}")
        sys.exit(1)



