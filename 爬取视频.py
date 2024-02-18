import requests
url='https://2059262482.qnqcdn.net:22443/qn-OTJBxVtoXKCFWIBAkVCUkI1EnGmQUMT4.vodkgeyttp8.vod.126.net/cloudmusic/MGAiJSAgNDUwJGAwZTAiOA==/mv/5368094/883bb43d3704dd9f37d0fe499a20e34b.mp4?wsSecret=061e6c956f47b7c774302c321aa842de&wsTime=1704773854'
from fake_useragent import UserAgent
U_A=UserAgent().random
header={
    'Uesr-Agent':U_A
}
res=requests.get(url,headers=header)
with open('starboy.mp4','wb') as f:
    f.write(res.content)