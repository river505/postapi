![image](https://github.com/river505/postapi/assets/98887550/a17753f7-267b-44fa-a17e-1d4eedcdb42c)### 快速上手--打分测评
```
git clone https://github.com/river505/postapi.git

cd postapi

pip install -r requirements.txt
```
#### 以测评zephyr-7B模型在theorem上的表现为例，使用qwen72B进行打分。
确保服务器端或本地启动了zephyr-7B模型，并使用openai接口规范（大部分框架都支持这一接口）
以LLama Factory为例，安装LLama Factory之后，在其根目录中，添加如下sh文件，注意修改路径。
以zephyr为例
```
CUDA_VISIBLE_DEVICES=0 API_PORT=8000 python src/api_demo.py \
    --model_name_or_path /models/zephyr \
    --template mistral
```
执行该sh，待模型启动成功后，使用本项目代码进行测评。
将待测评的alpaca格式数据放入datasets文件夹。

#### 1.windows系统：
修改reading.py文件内路径信息,假设我的文件为theorem_results.json，代码如下
```
def reading(filename=os.path.join(this,'dataset/theorem_results.json')): #第四行
```

保存后打开post-2.py, 修改最后一行的保存位置：
```
pd.Series(anslist).to_csv("./outputs/theorem_zephyr.csv", index=False) #第45行
```
保存后
执行post-2.py
```
python post-2.py
```
等待获取结果，获取结果后，进行72B打分过程，修改qwen72B_csv.py中的路径，为你刚刚获取的结果,并修改最后的得分保存路径：
```
test=pd.read_csv("./outputs/theorem_zephyr.csv",encoding="utf8")  #第6行

···

pd.Series(anslist).to_csv("./outputs/theorem_qwen14b_score.csv",encoding="utf8") #第46行
```
执行qwen72B_csv.py获取最后打分结果
```
python qwen72B_csv.py
```

#### 2.linux或macos
修改如下脚本内的位置信息,改为自己需要的路径，文件中三个参数以此为，读取路径、输出路径、url
```
#get_answer.sh
para_dataset='C:\Users\user\PycharmProjects\postapi\dataset\theorem_results.json'
para_outdir='./outputs/test1'
para_url='http://localhost:8000/v1/chat/completions'
#调用py脚本，并传递参数
python post-3.py $para_dataset $para_outdir $para_url
```
```
#get_score.sh
para_answer='./outputs/test1.csv'
para_score='./outputs/theorem_qwen14b_score.csv'
para_url='http://ty1.puhuacloud.com:20164/v1/chat/completions'
#调用py脚本，并传递参数
python post-3.py $para_answer $para_score $para_url
```
模型启动后，现执行get_answer.sh获取返回后，执行get_score.sh获得分数



## 本项目对各类模型应用发出post请求。
主要应用：

1.服务端启动LLamaFactory后，本地发出请求获得结果并保存（post.py,post-2.py）

2.模型客观打分。调整prompt，按1的应用获取回答后，可设计函数计算准确率

3.模型主观问题打分。当前项目版本中，将需要测试的原始文件json放入dataset，使用post-2.py获取服务端启动的模型的返回。获得返回后，使用qwen72b-csv.py获得qwen72b的评价结果。

**注意每次使用前，必须注意修改三项（两种）内容：api地址，读取的文件名，保存的文件名**

|文件/文件夹| 描述                                             |
|-----|------------------------------------------------|
| datasets | 文件夹存放原始数据的json文件                               |                        |
|outpus| 为结果存放目录，其中later_check.py用于对已生成的文件进行客观（选择/填空）检测 |
|chatchat.py| 向chatchat发送单次post                              |
|chathcat_csv | 向chatchat发送由csv提取的多条post                       |
|post.py | 向LLama-factory发送post（由csv提取）                   |
|post-2.py | 向LLama-factory发送post并将答案和结果共同保存                |
|qwen72b.py | 向qwen72b发送post                                 |
|qwen72b_csv.py | 向qwen72b发送来自csv答案问题对，进行打分，prompt在文件内修改         |
|qwen72b_json.py | 向qwen72b发送来自json文件数据的post                      |
|reading.py | 读取json文件的工具函数                                  |


tips:对于打分问题，可尝试调整优化qwen72b_csv.py中的prompt，当前版本只是一个可应用的例子。
