import requests
from lib import reader, configs

# get current/set dictionary
settings = configs.load_settings()
_current = settings['dictionary']
URL_FORMAT = settings['url_format']
# get url format and api-key
API_KEY = configs.get_api_key(settings['dictionary'])


def lookup(word:str):
    url = URL_FORMAT.format(w=word, k=API_KEY)
    response = requests.get(url)
    if response.status_code == 200:
        try:
            return response.json()
        except:
            return 
    else:
        raise ValueError("API Request Failed.API Response had code [{}].".format(response.status_code))

def filter(result:list, pos: str=None, hom_only: bool=True):
    """"This function will filter dictionary lookup results
    according to parameters provided at command line."""
    filtered = result
    if hom_only is True:
        filtered = [r for r in filtered if r.get('hom') is not None]
    ## TODO: Need to improve POS filtering; some objects overlap (e.g. noun -> plural noun)
    if pos is not None:
        if pos == 'noun':
            filtered = [d for d in filtered if d.get('fl') in ['noun', 'plural noun', 'proper noun']]
        else:
            filtered = [d for d in filtered if d.get('fl') == pos]
    return filtered 