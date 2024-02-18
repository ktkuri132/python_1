#更多的User-Agent值防止反爬

#2.函数随机生成User-Agent
import requests
from fake_useragent import UserAgent
#print(UserAgent().random)      fake_uesragent使用方法

url=('http://www.baidu.com/')
header={
    'User-Agent':UserAgent().random     #生成的User-Agent可能会出问题
}
res=requests.get(url,headers=header)
print(res.content.decode())
