import requests
import json
from reading import reading
url = "http://localhost:7861/chat/knowledge_base_chat"

payload = json.dumps({
  "query": "根据 智能赋能流体力学展望_张伟伟 写一篇概要 小红书风格",
  "knowledge_base_name": "论文测试1",
  "top_k": 3,
  "score_threshold": 1,
  "stream": False,
  "model_name": "Qwen-72B",
  "temperature": 0.7,
  "max_tokens": 0,
  "prompt_name": "default"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}



list1,list2=reading()
url = "http://localhost:8000/v1/chat/completions"
correct=0
anslist=[]
j=0
response = requests.request("POST", url, headers=headers, data=payload)
temp=response.text
_,temp=temp.split("data: {")
temp="{"+temp
temp= json.loads(temp)
ans=temp["answer"].replace("\n\n","\n")
print(ans)

# print(ans)

