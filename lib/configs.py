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

def get_api_key(dictionary:str) -> str:
    creds = load_credentials()
    dict_creds = creds['dictionaries']
    if dictionary in dict_creds:
        try:
            return dict_creds[dictionary]['api_key']
        except:
            raise ValueError("No api-key found in credentials for '{}' dictionary.".format(dictionary))
    else:
        raise ValueError("No credential information stored for '{}' dictionary.".format(dictionary))

