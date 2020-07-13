import requests
import json


arq = open("Julio.json", 'r')
Dic = json.load(arq)
print(Dic)

r = requests.post("https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume", json=Dic)
print("Status code: ", r.status_code)
print(r.json())
~                
