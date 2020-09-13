import yaml 

def open_yaml_file(filename:str) -> dict:
    with open(filename) as in_file:
        contents = yaml.safe_load(in_file)
        in_file.close()
    return contents 

def load_settings(filename:str='.configs/settings.yml') -> dict:
    settings = open_yaml_file(filename)
    return settings 

def load_credentials(filename:str='.configs/credentials.yml') -> dict:
    creds = open_yaml_file(filename)
    return creds 

def get_current_dictionary() -> str:
    settings = load_settings()
    try:
        return settings['current_dictionary']
    except:
        raise ValueError("No set dictionary in settings. Use the set argument.")

def get_api_key() -> str:
    try:
        key_info = open_yaml_file('.configs/.api_key.yml')
    except:
        raise ValueError(".api_key.yml file not found in '.configs'. Use the --set_key command to add your API Key.")
    try:
        return key_info['api_key']
    except:
        raise ValueError("API Key not found.")


