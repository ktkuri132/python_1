#实现post请求，登录金山词霸搜索

#回顾get请求访问金山词霸

import requests
from fake_useragent import UserAgent
useragent=UserAgent().random
url='https://ifanyi.iciba.com/index.php?c=trans'
header={
        'User-Agent':useragent
 }
tran=input('输入要翻译的词:')
ori=input('原文:')
to=input('译文:')
da={
     'from':f'{ori}',
     'to':f'{to}',
     'q':f'{tran}'
 }
res=requests.post(url=url,headers=header,data=da)
import json
dic=json.loads(res.text)
print('译文为:'+dic['out'])









