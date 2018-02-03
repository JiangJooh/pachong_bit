import requests
url = 'https://www.amazon.cn/dp/B00R3VSEAC/ref=cngwdyfloorv2_recs_0/458-1599006-9950431?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2&pf_rd_r=3N4C24SQRJ7G60BKEB61&pf_rd_r=3N4C24SQRJ7G60BKEB61&pf_rd_t=36701&pf_rd_p=19fc3fc8-b320-45dc-a7e8-b4ecd543eea8&pf_rd_p=19fc3fc8-b320-45dc-a7e8-b4ecd543eea8&pf_rd_i=desktop'
'''
r = requests.get(url)
print(r.status_code)
print(r.encoding)
print(r.request.headers)

kv = {'User-Agent':'Mozilla/5.0'}
r2 = requests.get(url,headers=kv)
print(r2.request.headers)
'''
try:
    kv = {'User-Agent':'Mozilla/5.0'}
    r= requests.get(url,headers=kv)
    print(r.status_code)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:2000])
except:
    print('爬取失败')

