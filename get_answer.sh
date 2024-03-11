para_dataset='C:\Users\user\PycharmProjects\postapi\dataset\theorem_results.json'
para_outdir='./outputs/test1'
para_url='http://localhost:8000/v1/chat/completions'
#调用py脚本，并传递参数
python post-3.py $para_dataset $para_outdir $para_url