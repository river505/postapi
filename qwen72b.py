import requests
import json
# import pandas as pd
# from reading import reading
# list1,list2=reading()
url = "http://ty1.puhuacloud.com:20164/v1/chat/completions"
correct=0
anslist=[]
j=0
for i in range(1):
  payload = json.dumps({
    "model": "string",
    "messages": [
      {
        "role": "user",
        "content": "如何评价中国地质大学"
      }
    ],
    "tools": [],
    "do_sample": True,
    "temperature": 0,
    "top_p": 0,
    "n": 1,
    "max_tokens": 1024,
    "stream": False
  })
  headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  ans=response.json()["choices"][0]["message"]["content"]
  # anslist.append(ans)
  print(ans)

