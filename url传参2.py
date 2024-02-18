import requests
from fake_useragent import UserAgent

url='http://www.baidu.com/S?'
wd={
    'wd':input('输入：')       #设置搜索参数wd
}
useragent=UserAgent().random
U_A={
    'User-Agent':useragent
}
res=requests.get(url,headers=U_A,params=wd)     #利用params函数代入参数wd
print(res.content.decode())     #快捷键crl+f在run出窗口调出搜索栏