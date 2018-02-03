import requests
import os

url = 'https://pic4.zhimg.com/80/v2-7f00214b92698e69d23f30c6d48603a0_hd.jpg'
root = 'F:/Python_program/pachong/pachong/'
path = root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件保存失败')
except:
    print('爬取失败')