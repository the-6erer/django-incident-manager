import requests
import json

def callGetEndpoint(endpoint):
    url = "http://localhost:8000/status/%s?format=json" % (endpoint)
    #headers = {'Authorization': 'Token deb6169c769943945ad8875c75514ea992e33c9a'}
    r = requests.get(url)
    j = json.loads(r.text)
    return j