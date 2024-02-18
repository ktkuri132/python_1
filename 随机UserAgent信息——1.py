#更多的User-Agent值防止反爬

#1.手动添加User-Agent的值：
import requests     #引用requests库

import random       #引用random库，它可以从一个列表中随机选出

User_Agent_bank=[     #创建一个伪装用户的库
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
]       #分别用不同的浏览器或不同的设备

UserAgent=random.choice(User_Agent_bank)    #使用ranom库中的choice方法从User_Agent_bank中随机挑选

User_Agent={
    'User-Agent':UserAgent
}

url=('http://www.baidu.com/')     #设置目标url

res=requests.get(url,headers=User_Agent)    #用requests库中的get方法/get请求，填入参数

print(res.content.decode())     #打印出相应内容，以二进制的格式解码

