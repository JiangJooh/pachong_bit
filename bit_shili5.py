import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30) 
        r.raise_for_status()#产生异常信息
        r.encoding = r.apparent_encoding
        return r.text #r是你get到的信息
    except:
        print('出现错误')
    print('getHtml over')

def fillUnivList(ulist,html):
    '''提取html中关键信息，并填写到列表中'''
    soup = BeautifulSoup(html,'html.parser')#html解析器
    for tr in soup.find('tbody').children:#每一个tr就对应一所大学的信息
        if isinstance(tr,bs4.element.Tag):#监测tr标签，监测是否是tag类型
            #tr标签已经监测出来，需要对td标签进行提取
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string])#排名学校省份
    print('fillUniv over')
   # print(ulist)

def printUnivList(ulist,num):
    print('{:^10}\t{:^6}\t{:^10}'.format('排名','学校名称','得分'))
    #print(type(ulist))
    for i in range(num):
        u = ulist[i]
        #print(type(u))
        print('{:^10}\t{:^6}\t{:^10}'.format(str(i+1),u[1],u[2]))
    print('printUniv over')

def main():
    uinfo = []#存放大学信息
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html#top'
    html = getHTMLText(url)#将url转换成html
    #将html中的信息转换后放到uinfo的列表中
    fillUnivList(uinfo,html)
    #输出
    printUnivList(uinfo,20)

if __name__ == '__main__' :
    print('主函数开始执行爬取信息')
    main()