import json
import requests
import time

#Open file with key on my PC to get url to my hue bridge
with open('C:\\Users\\charm\\OneDrive\\Desktop\\Christmas Turkey') as f:
    base_url = f.read().strip()

#Turning off first to make sure it's running
response = requests.put(base_url + 'lights/1/state', json.dumps({'on': False}))
print(response.content)
#Wait a second
time.sleep(3)
#Turn back on
response = requests.put(base_url + 'lights/1/state', json.dumps({'on': True}))
print(response.content)

