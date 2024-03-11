import requests
import json
import pandas as pd
from reading import reading
list1,list2=reading()
# test=pd.read_csv("./outputs/theorem_qwen14b.csv",encoding="utf8")

url = "http://ty1.puhuacloud.com:20164/v1/chat/completions"

correct=0

anslist=[]

total=0

j=0
for i in range(len(list1)):
  payload = json.dumps({
    "model": "string",
    "messages": [
      {
        "role": "user",
        "content": "这里有一些问答对，请你对回答进行考查并打分，问题和答案如下 \\n answer"+list1[i]+"###\\n" + "answer:"+list2[i]+"\n ###对答案进行评分需要客观，给出一个小数即可，0表示最差，1表示最好，不要有文字描述，仅直接输出数字，保留4位有效数字"
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
  total+=float(str(ans))
  print(total)
  anslist.append(ans)
  # print(ans)
anslist.append(total/len(list1))
pd.Series(anslist).to_csv("./outputs/theorem_ori_score.csv",encoding="utf8")
print(total/len(list1))