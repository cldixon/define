import requests
from lib import reader, configs

# get current/set dictionary
settings = configs.load_settings()
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
