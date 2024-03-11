para_answer='../outputs/test1.csv'
para_score='./outputs/theorem_qwen14b_score.csv'
para_url='http://ty1.puhuacloud.com:20164/v1/chat/completions'
#调用py脚本，并传递参数
python post-3.py $para_answer $para_score $para_url