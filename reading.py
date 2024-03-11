import json
import os
this=os.getcwd()
def reading(filename=os.path.join(this,'dataset/theorem_results.json')):
    with open(filename, mode='r', encoding='utf') as f:
        data = json.load(f)

    ans=data
    question_list=[]
    answers_list=[]
    for item in ans :
        str = item['instruction']
        str=str.replace('/n',"//n")
        # print(item['instruction'])
        question_list.append(str)
        answers_list.append(item['output'])
    # print(question_list)
    return question_list,answers_list

print(reading())