'''
淘宝页面搜索比价
'''
import requests
import re

def getHTMLText(url):#从url获取html信息
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding #将整体的编码替换成文本主体的编码
        print('完成html页面读取')
        return r.text
    except:
        return "error"
    


'''本例中没有使用bs4，而是直接使用搜索的策略'''
def parsePage(ilt,html):#解析页面
    try :
        plt = re.findall(r'"view_price":"[\d.]*"',html)
        tlt = re.findall(r'"raw_title":".*?"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print('error')
    print('完成页面解析，已将数据存入列表')


def printGoodList(ilt):#输出商品信息列表
    tplt = '{:4}\t{:8}\t{:16}'
    print(tplt.format('序号','价格','商品名称'))
    count = 0
    for g in ilt:
        count = count+1
        print(tplt.format(count,g[0],g[1]))
    
    print('打印完成')

def main():
    goods = '熊' #设计搜索内容
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




if __name__ == '__main__':
    print('begin')
    main()
    print('主函数执行完毕')

