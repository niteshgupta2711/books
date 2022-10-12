import json
import requests
url='http://127.0.0.1:8000/models'
json_string=json.dumps({'model':'knn'})
req=requests.post(url=url,data=json_string)
print(req.text)
