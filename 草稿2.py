import requests

url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%AD%A6%E4%B9%A0&fenlei=256&rsv_pq=0x9761764300634f2f&rsv_t=251aBWrpo8lvRtunSwQHs5hTxhBlc63AHtVgG%2BM0s1LathQPG4QP0is0ta9a&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=7&rsv_sug1=6&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&inputT=1738&rsv_sug4=3065&rsv_sug=1'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
res=requests.get(url,headers=header)
print(res.content.decode())
