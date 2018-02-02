import requests 

r = requests.get('http://www.baidu.com')
print(r.status_code)
print(r.text)
print(r.content)

r.encoding = 'uft-8'
print(r.text)