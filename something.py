import requests
import json
import os

def get_epub(dir):
    return [file for file in os.listdir(dir) if file.endswith('.epub') ]
url = 'https://api.jsonbin.io/v3/b/665295efe41b4d34e4f96e99'
headers = {
  'Content-Type': 'application/json',
  'X-Master-Key': '$2a$10$Sxm35XHa2DxDymTpdpjws.WJIghRt6HO3BcnHMUvsKxGaRfvTOm36'
}
for file in get_epub('.'):
  data = json.loads(open(file, 'r').read())
  req = requests.put(url, json=data, headers=headers)
  print(file)
