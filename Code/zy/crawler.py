import requests
import pymongo
from bs4 import BeautifulSoup

start_url = 'http://bj.58.com/sale.shtml'
url_host = 'http://bj.58.com'
#定义一个爬虫函数来获取二手市场页面中的全部大类页面的连接
def get_channel_urls(url):
    # 使用Requests库来进行一次请求
    web_data = requests.get(url)
    # 使用BeautifulSoup对获取到的页面进行解析
    soup = BeautifulSoup(web_data.text,'lxml')
    # 根据页面内的定位信息获取到全部大类所对应的连接
    urls = soup.select('ul.ym-submnu > li > b > a')
    #作这两行处理是因为有的标签有链接，但是却是空内容
    for link in urls:
        if link.text.isspace():
            continue
        else:
            page_url = url_host + link.get('href')
            print(page_url)
get_channel_urls(start_url)

client = pymongo.MongoClient('localhost',27017)#链接MongoDB
DB_58 = client['DB_58']#创建一个数据库
url_list_tab = DB_58['url_list_tab']#创建用于存储全部商品url的文档
item_detail_tab = DB_58['item_detail_tab']#创建用于存储商品详情的文档

#从每个频道获取全部的商品链接
def get_link_from(channel,pages,who_sells=0):
    #http://bj.58.com/diannao/0/pn5/
    list_view = '{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
    web_data = requests.get(list_view)
    time.sleep(2)
    soup = BeautifulSoup(web_data.text,'lxml')
    #爬取个人商家列表
    if soup.find('td','t'):
        for link in soup.select('.zzinfo > td.t >a.t'):
            item_link = link.get('href').split('?')[0]
            #去除掉跳转类型的连接
            if item_link != 'http://jump.zhineng.58.com/jump':
                #得到想要的商品页面链接之后保存在数据库中
                url_list_tab.insert_one({'url':item_link})
                print(item_link)
            else:
                pass
                # 爬取店铺商家列表
                if soup.find ('div', 'left'):
                    for link in soup.select ('a.title'):
                        item_link = link.get ('href')
                        # 去除掉跳转类型的连接
                        if item_link != 'http://jump.zhineng.58.com/jump':
                            # 得到想要的商品页面链接之后保存在数据库中
                            url_list_tab.insert_one ({'url': item_link})
                            print (item_link)
                else:
                    pass
