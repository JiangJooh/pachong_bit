'''
淘宝页面搜索比价
'''
import requests
import re

def getHTMLText(url):#从url获取html信息
    pass 

def parsePage(ilt,html):#解析页面
    pass

def printGoodList(ilt):#输出商品信息列表
    print('')

def main():
    goods = '联想' #设计搜索内容
    depth = 3 #设定爬取深度，这里我们设计爬取第123页
    start_url = 'https://s.taobao.com/search?q='+goods
    infoList = []
    #由于每一页面访问的url不同，所以，采用for循环进行爬取
    for i in range(depth):
        try:
            url = start_url+'&s='+str(44*i)
            #https://s.taobao.com/search?q=%E8%81%94%E6%83%B3&s=44
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodList(infoList)





if '__name__' == '__main__':
    main()
    print('主函数执行完毕')


