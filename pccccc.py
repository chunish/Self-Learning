# -*- coding:UTF-8 -*-  
import requests
from bs4 import BeautifulSoup
import os
headers = {'User-Agent':"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36"}##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
all_url = 'http://www.90ssss.com/p03/index.html'  ##开始的URL地址
hed_url =  'http://www.90ssss.com'
start_html = requests.get(all_url,  headers=headers)  ##使用requests中的get方法来获取all_url(就是：http://www.mz
Soup = BeautifulSoup(start_html.text, 'lxml')

i=0


def tr_img(url,path):
    start_html = requests.get(url,  headers=headers)  ##使用requests中的get方法来获取all_url(就是：http://www.mz
    Soup = BeautifulSoup(start_html.text, 'lxml')
    all_img = Soup.find('div',class_="left1").find_all("img")
    for img in all_img:
        src_url = img['src']
        print(src_url)

        name = src_url[-5:-4] ##取URL 倒数第四至第九位 做图片的名字
        imgg = requests.get(src_url, headers=headers)
        f = open(path+name+'.jpg', 'ab')##写入多媒体文件必须要 b 这个参数！！必须要！！
        f.write(imgg.content) ##多媒体文件要是用conctent哦！
        f.close()
        


i = 0
all_a = Soup.find('div', class_='typelist').find_all('a') ##意思是先查找 class为 all 的div标签，然后查找所有的<a>标签。
for a in all_a:
    title = a.get_text()
    #path = str(title).strip() ##去掉空格
    #print(path)
    os.makedirs(os.path.join("mzitu", str(i))) ##创建一个存放套图的文件夹
    
    href = a['href']
    page_url = hed_url+href
    img_html = requests.get(page_url, headers = headers)
    img_Soup = BeautifulSoup(img_html.text, 'lxml') 
    img_html = requests.get(page_url,  headers=headers)  ##使用requests中的get方法来获取all_url(就是：http://www.mz
    img_Soup = BeautifulSoup(img_html.text, 'lxml')
    all_img = img_Soup.find('div',class_="left1").find_all("img")
    j =10
    for img in all_img:
        src_url = img['src']
        print(src_url)

        name = src_url[-5:-4] ##取URL 倒数第四至第九位 做图片的名字
        imgg = requests.get(src_url, headers=headers)
        f = open(os.path.join("mzitu", str(i),str(j)+'.jpg'), 'ab')##写入多媒体文件必须要 b 这个参数！！必须要！！
        f.write(imgg.content) ##多媒体文件要是用conctent哦！
        f.close()
        j=j+1
    i=i+1
