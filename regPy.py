import requests
import json
js={'content-type':'application/json'}
url = 'https://cit-home1.herokuapp.com/api/register'
r = requests.post(url,{},json.dumps(js))
print(r.json()['answer'])
url = 'https://cit-home1.herokuapp.com/api/check_me'
r = requests.get(url)
print(r.json())
