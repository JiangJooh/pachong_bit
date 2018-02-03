'''模拟搜索引擎'''

import requests
'''kv = {'wd':'Python'}
r=requests.get('http://www.baidu.com/s',params=kv)
print(r.status_code)

print(r.request.url)
'''
#wd 表示接口，Python表示接口的值
keyword = '你好'
try:
    kv = {'wd':keyword}
    r = requests.get('http://www.baidu.com/s',params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except :
    print('爬取失败')