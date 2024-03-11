import json
import os
import pandas as pd
this=os.getcwd()
pd.set_option('display.width', 2000)

def reading(filename=os.path.join(this,'../dataset/val_reclor_alpca.json')):
    with open(filename, mode='r', encoding='utf') as f:
        data = json.load(f)
    ans = data
    question_list = []
    answers_list = []
    for item in ans:
        str = item['instruction']
        str = str.replace('/n', "//n")
        # print(item['instruction'])
        question_list.append(str)
        answers_list.append(item['output'])
    # print(question_list)
    return question_list, answers_list
_,anslist=reading()

this=os.getcwd()
ans = pd.read_csv("qwen_ori_reclor.csv")
print(ans)
correct=0
for i in range(len(anslist)):
    if anslist[i] == str(ans['0'].iloc[i])[0]:
        correct+=1
print(correct/len(anslist))