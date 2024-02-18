from urllib.parse import quote,unquote
#quote明文加密
print(quote('学习'))
#unquote密文翻译
print(unquote('%E5%AD%A6%E4%B9%A0'))



#1.通过格式化f携带参数,模拟浏览器的行为
#*******************************************************
name=input('输入:')
name_quote=quote('name')
url=f'http://www.baidu.com/S?wd={name_quote}'
import requests
from fake_useragent import UserAgent
U_A=UserAgent().random
useragent={
    'User-Agent':U_A
}
res=requests.get(url,headers=useragent)
print(res.content.decode())