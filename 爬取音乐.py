import requests
url='https://m801.music.126.net/20240109123846/8b1f01c0c93c5d3fc763e30b390c69eb/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/28942598693/ece3/1e4d/871f/1949ceba0658e5632f986f82619ddaa3.m4a'
header={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
res=requests.get(url,headers=header)
#print(res.content)
with open('one of the girl.mp3','wb') as f:
    f.write(res.content)