import random
import time
import requests
from fake_useragent import UserAgent
#https://tieba.baidu.com/f?kw=%E5%8B%BE&ie=utf-8&pn=0
url='https://tieba.baidu.com/f?'
IP=[
    '114.231.42.64:8888'
    '58.220.95.86:9401'
]
IP_add={
    'http':'http://'+random.choice(IP)
}
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
name=input('输入名字:')
page=int(input('输入页面:'))


for i in range(page):
    params={
        'kw':name,
        'pn':i*50,
    }
    res=requests.get(url,headers=header,params=params,proxies=IP_add)
    with open(f'{name}贴吧{i+1}.html','wb') as f:
        f.write(res.content)
    #time.sleep(1.0)