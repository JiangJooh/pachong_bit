import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url):
    #print('开始获取URL信息')
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    #print('获取URL信息完毕')

def getStockList(lst,stockURL):
    print('开始获取网站上的股票列表')
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html,'html.parser')
    a = soup.find_all('a')
    '''
     <li><a target="_blank" href="http://quote.eastmoney.com/sh201000.html">R003(201000)</a></li>
    '''
    #for i in a:
    for i in a:
        try:
            #个股的股票编号保存在lst中
            href = i.attrs['href']
            #print(type(href))
            lst.append(re.findall(r'[s][hz]\d{6}',href)[0])
            #findall返回列表，比如a=[sh012345],取0，就取出了里面的数字
            #在append到lst里，这样lst就不会是[[sh201000], [sh201002]]这样
        except:
            continue
    print('获取股票列表完毕')

def getStockInfo(lst,stockURL,fpath):
    print('开始获取股票信息')
    for stock in lst:
        url = stockURL+stock+'.html'
        html = getHTMLText(url)
        try:
            if html=='':
                continue 
            infoDict = {}
            soup = BeautifulSoup(html,'html.parser')
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})#获取当前股票所在的div标签
            #print(stockInfo)
            # find 返回一个字符串
            # find_all 返回一个列表

            #获取股票名字
            name = soup.find('a',attrs = {'class':'bets-name'})
            #print(type(name)) 标签类
            #print(name)
            jijin = re.findall(r'[A-Z0-9]+',str(name))
            print(jijin[0])
            print(name.text)
            infoDict.update({'股票名称':name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')#找到股票信息的两个键、值标签
            #将键值对还原成键值对，并存到字典中
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key]=val

            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infoDict)+'\n')

        except:
            traceback.print_exc()
            continue
    print('开始获取股票信息')



def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'F://BaiduStockInfo.txt'
    slist = []#股票信息
    #首先获取股票列表
    getStockList(slist,stock_list_url)
    #根据股票列表到相关网站获取信息
    getStockInfo(slist,stock_info_url,output_file)
if __name__ =='__main__':
    print('主函数开始执行')
    main()
    print('主函数执行完毕')