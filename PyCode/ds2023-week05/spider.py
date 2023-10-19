import xml
import csv
import requests
from lxml import etree

with open('movie_data.csv','w',newline='', encoding='utf-8') as fp:
    writer = csv.writer(fp)

#<程序6.2：网络爬虫>
#1.先定义要爬取的宁段
    # writer.writerow(('name','actor','infomation','date','star','evaluate','introduction'))
    writer.writerow(['name'])
#2.定义要爬取的链接及设置header相关参数
    urls=['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0,250,25)]
    headers ={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36'}
#3.通过reguest 请求访问网页并几获取网页内容
    for url in urls:
        html =requests.get(url, headers=headers)
        selector = etree.HTML(html.text)
    #catch html text 
        infos=selector.xpath("//ol[@class='grid_view']/li")#visit all the urls and get information
#4.解析网页内容
        for info in infos:
            name=info.xpath(".//div[@class='info']//div[@class='hd']//a/span[1]/text()")
            writer.writerow((name))