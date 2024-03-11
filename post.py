import requests
import json
from reading import reading
import pandas as pd
list1,list2=reading()
url = "http://localhost:8000/v1/chat/completions"
correct=0
anslist=[]
j=0
for i in list1:
  payload = json.dumps({
    "model": "string",
    "messages": [
      {
        "role": "user",
        "content": "范德瓦尔斯方程是什么？"
      }
    ],
    "tools": [],
    "do_sample": True,
    "temperature": 0,
    "top_p": 0,
    "n": 1,
    "max_tokens": 0,
    "stream": False
  })
  headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
  }


  response = requests.request("POST", url, headers=headers, data=payload)
  ans=response.json()["choices"][0]["message"]["content"]
  ans = ans.replace("\n","\\n")
  ans = "question: \\n"+ i + "###\\n" + "answer: \\n"+ans
  anslist.append(ans)
  # if list2[j] in ans:
  #   correct+=1
  # j+=1
  print(ans)

# print(correct/len(list2))
pd.Series(anslist).to_csv("./outputs/theorem_zephyr.csv", index=False)


