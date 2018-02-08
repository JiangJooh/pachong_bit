import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    
    return ""

def fillUnivList(ulist,html):
    pass

def printUnivList(ulist,num):
    print('Suc' + str(num))

def main():
    uinfo = []#存放大学信息
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2017.html#top'
    html = getHTMLText(url)#将url转换成html
    #将html中的信息转换后放到uinfo的列表中
    fillUnivList(uinfo,html)
    #输出
    printUnivList(uinfo,20)

if __name__ == '__main__' :
    print('主函数开始执行爬取信息')
    main()