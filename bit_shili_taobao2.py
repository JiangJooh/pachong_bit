'''未完成'''

import requests
import re
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    print('开始获取网页信息')
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
        print('获取网页信息成功')
    except:
        print('获取网页信息失败')

def parsePage(ilt,html):
    soup = BeautifulSoup(html,'html.parser')
    print(soup.prettify())
    for strong in soup.find('div')
    a=[]
    price = re.findall(r'<strong>[\d.]*',soup)
    print(price)
    for i in range(len(price)):
        price_num = eval(price[i].split('>')[1])
        a.append(price_num)
    print(a)
    

def printGoodList(ilt):
    pass

def main():
    #设定请求内容
    goods = '联想'
    #设定爬取深度
    depth = 3
    start_url = 'https://s.taobao.com/search?q='+goods
    infoList = []

    #对不同的页面循环爬取
    for i in range(depth):
        try:
            url = start_url+'&s='+str(44*i)
            print('爬取的URL为：'+url)
            html = getHTMLText(url)#r.text
            parsePage(infoList,html)#对页面解析
        except :
            print('出现异常')
            continue
        printGoodList(infoList)

if __name__ == '__main__':
    print('程序开始执行')
    main()
    print('程序执行完毕')
