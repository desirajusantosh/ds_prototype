import requests
from data_input import data

URL = 'http://127.0.0.1:5000/predict'

headers = {"Content-Type": "application/json"}
data_in = {"input": data}

r = requests.get(URL,headers=headers, json=data_in) 

print(r.json())
