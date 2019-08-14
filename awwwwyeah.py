import json
import requests
import time
with open('C:\\Users\\charm\\OneDrive\\Desktop\\Christmas Turkey') as f:
    base_url = f.read().strip()
response = requests.put(base_url + 'lights/1/state', json.dumps({'on': False}))
print(response.content)
time.sleep(3)
response = requests.put(base_url + 'lights/1/state', json.dumps({'on': True}))
print(response.content)