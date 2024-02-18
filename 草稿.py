import requests
from urllib.parse import quote,unquote

class bing:
    def __init__(self,key_word,page):
        self.url=f'https://www.baidu.com/s?'
        self.keyword=key_word
        self.page=page
        self.headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
            'Cookie':'BIDUPSID=899A4421517EE4449876ABACC0395DFF; PSTM=1704614724; BDSFRCVID=SN0OJeC62Raq8hTqwWD6EHtYoU9DKPbTH6aooqNH8jVDTR_Uz8gzEG0Pcx8g0KuMn6bMogKKLgOTHUQNc2L28A3PomAJ35lUumP1tf8g0x5; H_BDCLCKID_SF=JnIOoCIMtID3qnFkKJL_-P4DenbwJURZ5mAqofoq-CnsS-j63U8-Qfk3WfnPqx3iLIrnaIQqab7a8lP9MljU3hDm3qCOKbT43bRT3-Py5KJvfq6kj45YhP-UyPvMWh37QG6w3Ko1tDnNhUJvhfQkDTLj3qoLQToJ5JbMoPPafJOKHICme5D-DUK; BDSFRCVID_BFESS=SN0OJeC62Raq8hTqwWD6EHtYoU9DKPbTH6aooqNH8jVDTR_Uz8gzEG0Pcx8g0KuMn6bMogKKLgOTHUQNc2L28A3PomAJ35lUumP1tf8g0x5; H_BDCLCKID_SF_BFESS=JnIOoCIMtID3qnFkKJL_-P4DenbwJURZ5mAqofoq-CnsS-j63U8-Qfk3WfnPqx3iLIrnaIQqab7a8lP9MljU3hDm3qCOKbT43bRT3-Py5KJvfq6kj45YhP-UyPvMWh37QG6w3Ko1tDnNhUJvhfQkDTLj3qoLQToJ5JbMoPPafJOKHICme5D-DUK; BD_CK_SAM=1; BAIDUID=40A8E9D9DD0B284E74F42E6E4C83187A:FG=1; BAIDUID_BFESS=40A8E9D9DD0B284E74F42E6E4C83187A:FG=1; delPer=0; ZFY=tqU4QdoOJK10Y03fDAA0L0BTkRzak3IzafRgbFiZrz0:C; BAIDU_WISE_UID=wapp_1704775707206_855; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1704894498; Hm_lpvt_aec699bb6442ba076c8981c6dc490771=1704894498; H_PS_PSSID=39997_40169_40201_40210_40206_40216_40223; BD_UPN=12314753; BA_HECTOR=a4a5a5808k8h04848h21a421h2e35b1it17ap1s; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=3; baikeVisitId=285458d1-4ee1-466b-a7c6-9b385676c05b; H_PS_645EC=9817tjodciNkPg7Kd7FPKesDFwxKDePc7BpN0sX6oYKV%2BLI02VaJQPI2r8E; BDSVRTM=205;',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',

            'Host':'www.baidu.com',
            'Connection':'keep-alive'

        }

        self.data='Sat, 17 Feb 2024 12:14:25 GMT'

        self.pa=0

        self.params={
            'wd':key_word,
            'pn':self.pa,
            'base_query':key_word,
            'oq':key_word,
            'ie':'utf-8'
        }
    def run(self):
        if self.page==1:
            pn=0
        elif self.page>1:
            pn=(self.page-1)*10
        res=requests.get(url=self.url,headers=self.headers,params=self.params)
        print(res.content.decode())

key_word=input('搜索:')
page=int(input('页数:'))
start=bing(f'{key_word}',page)

if __name__=='__main__':
    start.run()
    print('为什么不输出？？？（恼')
