#目标url
#设置参数
#发送请求
#获取响应，保存文件

import random

import requests
#创建一个贴吧的类
class tieba:        #类的可传参数
    def __init__(self,name,page,ip):
        self.url='https://tieba.baidu.com/f?'   #url为固定参数
        self.name=name
        self.page=int(page)
        self.header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
        }
        self.params={
            'kw':name,
            'pn':0
        }
        self.ip=ip
        self.IP=[
            '114.231.42.64:8888',
            '58.220.95.86:9401'
            ]
        self.ip_add={
            'http':'http://'+self.ip
        }
        #类的可用方法
    def run(self):
        if self.ip=='no':
            self.ip=random.choice(self.IP)
        for i in range(self.page):
            self.params['pn']=i
            res=requests.get(url=self.url,headers=self.header,params=self.params,proxies=self.ip_add)
            with open(f'{self.name}吧的第{i+1}页.html','wb') as f:
                f.write(res.content)

name=input('输入贴吧的名字：')
page=input('输入要爬取的页数：')
typ=input('输入代理的IP及端口(若没有填写no)：')
gouba=tieba(f'{name}',f'{page}',f'{typ}')

try:
    print('获取响应成功\n正在获取......')
    gouba.run()
    print('结束')
except:
    print('获取响应失败')