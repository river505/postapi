import requests
import json
from reading import reading
import pandas as pd
txt_1=""
txt_2=""

list1,list2=reading(txt_1)
list3,list4=reading(txt_2)

url = "http://localhost:8000/v1/chat/completions"
correct=0

anslist_a=[]


j=0
for m,n in list1:
  payload = json.dumps({
    "model": "string",
    "messages": [
      {
        "role": "user",
        "content": i+'## \n 注意：只输出一个数字，不要任何的修饰，不要有单词、字母！'
      }
    ],
    "tools": [],
    "do_sample": True,
    "temperature": 0,
    "top_p": 0,
    "n": 1,
    "max_tokens": 1000,
    "stream": False
  })
  headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  ans=response.json()["choices"][0]["message"]["content"]
  anslist.append(ans)
  if list2[j] in ans:
    correct+=1
  j+=1
  print(ans)

print(correct/len(list2))
pd.Series(anslist).to_csv("./outputs/qwen_ori_trained__reclor_promprconstraintX.csv", index=False)


