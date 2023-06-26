import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://api.seguradora.com.br/open-insurance/discovery/v1/status', headers = headers)


print(r.json())