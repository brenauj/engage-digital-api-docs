import requests

SERVER = "https://<YOUR-DOMAIN>.api.engagement.dimelo.com"
ACCESS_TOKEN = '<API-ACCESS-TOKEN>'
API = "/1.0/tasks"

try:
    url = SERVER + API
    headers = {
            'Authorization': 'Bearer ' + ACCESS_TOKEN
          }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print (response._content)
        else:
            print (response.status_code)
    except Exception as e:
        raise ValueError(e)
except Exception as e:
    raise ValueError(e)
