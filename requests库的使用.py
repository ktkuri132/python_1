import requests
#http://www.baidu.com/
url=('http://121.40.68.153')

header_0={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}       #加上User-Agent让服务器知道你是用户而不是python程序

x=requests.get(url,headers=header_0)    #请求方式，headers只能使用字典格式

print(x.content.decode())       #以二进制格式解码响应

#with open('aliyun.html','w',encoding='utf-8') as f:
    #f.write(x.content.decode())        将将相应内容保存到一个文件