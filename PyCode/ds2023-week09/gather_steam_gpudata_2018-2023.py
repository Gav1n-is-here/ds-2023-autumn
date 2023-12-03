import requests
from lxml import html
import xlwt  # 进行excel操作
import xlrd

etree = html.etree
headers = {
    
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/79.0.3945.130 Safari/537.36',
    'Connection':'close'
}


def fetch_and_write(urlin):
    url = urlin  
    s = requests.session()
    s.keep_alive = False
    proxies={
'http': 'http://127.0.0.1:7890',
'https': 'http://127.0.0.1:7890'  # https -> http
}

    html = requests.get(url, headers=headers, timeout=20,stream=True, verify=True,proxies=proxies)  
    xhtml = etree.HTML(html.content.decode("utf-8"))  # 解析网页

    #title格式不同
    #title=xhtml.xpath('//*[@id="hws_body"]/h1/text()')[0]
    #title=xhtml.xpath('//*[@id="hws_ctn"]/h1/text()')[0]
    title=xhtml.xpath('//*[@id="hws_ctn"]/div/h1/text()')[0]


    # //*[@id="sub_stats"]/div[21]/div[1]/text()
    # //*[@id="sub_stats"]/div[21]/div[6]/strong
    # gpustart='//*[@id="sub_stats"]/div[{}]/div[1]/text()'
    # perstart='//*[@id="sub_stats"]/div[{}]/div[6]/strong/text()'

    # 2019 april：
    # //*[@id="sub_stats"]/div[19]/div[1]/text()
    # //*[@id="sub_stats"]/div[19]/div[5]/strong
    # gpustart='//*[@id="sub_stats"]/div[{}]/div[1]/text()'
    # perstart='//*[@id="sub_stats"]/div[{}]/div[5]/strong/text()'

    # 2019 july:
    # //*[@id="sub_stats"]/div[21]/div[1]/text()
    # //*[@id="sub_stats"]/div[21]/div[6]/strong

    # 2019 december:
    # //*[@id="sub_stats"]/div[17]/div[1]/text()
    # //*[@id="sub_stats"]/div[17]/div[4]/strong
    # gpustart='//*[@id="sub_stats"]/div[{}]/div[1]/text()'
    # perstart='//*[@id="sub_stats"]/div[{}]/div[4]/strong/text()'



    
    

    # j=21  #5 col
    # gpustart='//*[@id="sub_stats"]/div[{}]/div[1]/text()'
    # perstart='//*[@id="sub_stats"]/div[{}]/div[6]/strong/text()'

    # j=19  #4 col
    # gpustart='//*[@id="sub_stats"]/div[{}]/div[1]/text()'
    # perstart='//*[@id="sub_stats"]/div[{}]/div[5]/strong/text()'

    # j=17  #3 rol
    # gpustart='//*[@id="sub_stats"]/div[{}]/div[1]/text()'
    # perstart='//*[@id="sub_stats"]/div[{}]/div[4]/strong/text()'

    j=21  # 2021 11 -2022 12
    gpustart='//*[@id="sub_stats"]/div[{}]/div[1]/div/span/text()'
    perstart='//*[@id="sub_stats"]/div[{}]/div[6]/strong/text()'
    
    # # 2023 01
    # j=19  #4 col
    # gpustart='//*[@id="sub_stats"]/div[{}]/div[1]/div/span/text()'
    # perstart='//*[@id="sub_stats"]/div[{}]/div[5]/strong/text()'
    


    gpuname=[]
    percentage=[]
    for i in range (0,30):
        a=xhtml.xpath(gpustart.format(j))[0]
        b=xhtml.xpath(perstart.format(j))[0]

        gpuname.append(a)
        percentage.append(b)
        j=j+1



    data = xlrd.open_workbook('gpu.xls',formatting_info=True)
    from xlutils.copy import copy
    book = copy(wb=data) # 完成xlrd对象向xlwt对象转换
    # book = xlwt.Workbook(encoding="utf-8",style_compression=0) #创建workbook对象
    try:
        sheet = book.add_sheet(title[34:], cell_overwrite_ok=True) #创建工作表
        col = ('gpuname','percentage')
        for i in range(0,2):
                sheet.write(0,i,col[i])  #列名S
        for i in range(0,30):
            sheet.write(i+1,0,gpuname[i])
            sheet.write(i+1,1,percentage[i])
    
        book.save('gpu.xls') #保存
    except IndexError as e:
        print (e)
        pass


# 2018
#fetch_and_write("https://web.archive.org/web/20180213195357/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20180316033342/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20180425133034/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20180515133037/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20180612133103/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20180710005013/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20180830170047/https://store.steampowered.com/hwsurvey/videocard/")
#fetch_and_write("https://web.archive.org/web/20180925133644/https://store.steampowered.com/hwsurvey/videocard/")
#fetch_and_write("https://web.archive.org/web/20181029110534/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20181105143022/https://store.steampowered.com/hwsurvey/videocard/")
#fetch_and_write("https://web.archive.org/web/20181210143021/https://store.steampowered.com/hwsurvey/videocard/")
#fetch_and_write("https://web.archive.org/web/20190105143028/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20190105143028/https://store.steampowered.com/hwsurvey/videocard/")

#2019
# fetch_and_write("https://web.archive.org/web/20190205143018/https://store.steampowered.com/hwsurvey/videocard/")
#fetch_and_write("https://web.archive.org/web/20190331053919/https://store.steampowered.com/hwsurvey/videocard/")
#fetch_and_write("https://web.archive.org/web/20190409092426/https://store.steampowered.com/hwsurvey/videocard/")
#fetch_and_write("https://web.archive.org/web/20190531134032/https://store.steampowered.com/hwsurvey/videocard/")
#fetch_and_write("https://web.archive.org/web/20190630120008/https://store.steampowered.com/hwsurvey/videocard/")
#fetch_and_write("https://web.archive.org/web/20190731144747/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20190827184131/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20190923162216/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20191021144317/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20191115221225/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20191229170927/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20200131203548/https://store.steampowered.com/hwsurvey/videocard/")

#2020
# fetch_and_write("https://web.archive.org/web/20200214042735/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20200331130631/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20200429042430/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20200505031406/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20200630132218/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20200712230514/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20200817071905/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20200930142622/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20201004074127/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20201127094650/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20201223132937/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20210123210719/https://store.steampowered.com/hwsurvey/videocard/")

# 2021
# fetch_and_write("https://web.archive.org/web/20210215152300/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20210331141251/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20210430002527/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20210504105024/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20210606073435/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20210706033055/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20210831130636/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20210930094308/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20211006163933/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20211102090820/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20211227112046/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20220127130937/https://store.steampowered.com/hwsurvey/videocard/")

#2022
# fetch_and_write("https://web.archive.org/web/20220228133945/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20220313142227/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20220403072338/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20220526020335/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20220614192137/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20220716105550/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20220831141652/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20220920153512/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20221018143153/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20221128163946/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20221215023505/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20230102112508/https://store.steampowered.com/hwsurvey/videocard/")

# 2023
# fetch_and_write("https://web.archive.org/web/20230215122423/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20230315055009/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20230418002819/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20230528201416/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20230629015440/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20230724152147/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20230822105257/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20230912201315/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://web.archive.org/web/20231025073946/https://store.steampowered.com/hwsurvey/videocard/")
# fetch_and_write("https://store.steampowered.com/hwsurvey/videocard/")
