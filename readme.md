#   Postapi
### 本项目对各类模型应用发出post请求。
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


tips对于打分问题，可尝试调整优化qwen72b_csv.py中的prompt，当前版本只是一个可应用的例子。
