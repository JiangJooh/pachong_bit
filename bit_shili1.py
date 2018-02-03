'''
https://item.jd.com/3133927.html
'''
import requests 
url = 'https://item.jd.com/3133927.html'
try:
    r = requests.get(url)
    r.raise_for_status()#返回代码是200时，正常，不会抛出异常
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except :
    print('爬取失败')