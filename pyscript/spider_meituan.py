# -*- coding:utf-8
import requests
from bs4 import BeautifulSoup  # 解析网页
import time
import json

import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = 'http://bj.meituan.com/'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'waimai.meituan.com',
    'Referer': 'http://www.meituan.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Content-Type': 'text/html; charset=utf-8',
    'Cookie': 'uuid=93eeb40470d24d05814d.1520677399.1.0.0; _lxsdk_cuid=1620f6fd2dbc8-09af7ad33673e5-b353461-100200-1620f6fd2dcc8; ci=1; w_utmz="utm_campaign=(direct)&utm_source=(direct)&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; w_uuid=RMmDxguW7Bsf1EF6SyfghIZzx-EUEzvOG1xBCCJrVZASRe1Tw1G0my7_iH3Yhb8G; _ga=GA1.3.1386576474.1520677422; _gid=GA1.3.1743985992.1520677422; IJSESSIONID=19qko9xvf962d1h1vino6chn0k; iuuid=2CFE06D77DDD28049A2C92CE237E16CB50F6BFD501015852B6FB0353FD8395B4; cityname=%E5%8C%97%E4%BA%AC; backurl=http://i.waimai.meituan.com/home?lat=37.434075&lng=122.196679; mtcdn=K; i_extend=H__a100040__b1; webp=1; __utma=74597006.776767663.1520679397.1520679397.1520679397.1; __utmc=74597006; __utmz=74597006.1520679397.1.1.utmcsr=i.waimai.meituan.com|utmccn=(referral)|utmcmd=referral|utmcct=/home; waddrname="%E4%BA%9A%E4%BF%A1%E6%80%BB%E9%83%A8%E7%A0%94%E5%8F%91%E4%B8%AD%E5%BF%83%E5%A4%A7%E5%8E%A6"; w_geoid=wx4ey4vz1qqj; w_cid=110108; w_cpy=haidianqu; w_cpy_cn="%E6%B5%B7%E6%B7%80%E5%8C%BA"; w_ah="40.05052188411355,116.28725498914719,%E4%BA%9A%E4%BF%A1%E6%80%BB%E9%83%A8%E7%A0%94%E5%8F%91%E4%B8%AD%E5%BF%83%E5%A4%A7%E5%8E%A6"; rvct=1; lat=39.854247; lng=116.398873; __mta=190051604.1520677410298.1520683739763.1520683891262.3; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; w_visitid=ed722cf4-d297-47ee-916d-c1fbc2d57a53; JSESSIONID=q2yuz48g9fl0u2d9wj4qqsc4; __mta=190051604.1520677410298.1520683891262.1520754705993.4; _lxsdk_s=16213fb7024-d39-575-29%7C%7C10'
}


# 获取美团主页源码,以得到店铺分类（美食，外卖...）
def get_home(url):
    home_html = requests.get(url).content  # 获取主页文本
    soup = BeautifulSoup(home_html, 'html.parser')  # 解析网页
    links = []
    for link in soup.find_all('li', class_='nav-li'):
        child_link = link.find('span')
        for span in child_link.find_all('span'):
            links.append(span.find('a')['href'])
    return links


# 获取每个分类链接中的店铺id
def get_store_id(url, headers):
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    content_id = 1


def get_yaxin_waimai(headers):
    yaxin_url = 'http://waimai.meituan.com/home/wx4ey4vz1qqj'
    html = requests.get(yaxin_url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    store_bases = []
    for div in soup.find_all('div', class_='restaurant'):
        store_id = div['data-poiid']
        store_name = div['data-title']
        store_bases.append([store_id, store_name])
    restaurant_url = 'http://waimai.meituan.com/restaurant/'
    comment_url = 'http://waimai.meituan.com/comment/'
    info = []
    index = 0
    for store_base in store_bases:
        index += 1
        print '正在爬取第 ', index, ' 家店信息 ', store_base[0]
        store_url0 = restaurant_url + store_base[0]
        store_url1 = comment_url + store_base[0]
        html0 = requests.get(store_url0, headers=headers).text
        soup0 = BeautifulSoup(html0, 'html.parser')
        if soup0.find('p', class_='notsupport-comment'):
            print '当前店家不支持PC展示店铺'
            index -= 1
            time.sleep(5)
            continue
        rank = soup0.find('span', class_='fl mark ct-middlegrey').text
        avg_time = soup0.find('div', class_='fl average-speed').find('div', class_='nu').find('strong').text + '分钟'  # 平均送餐时间
        base_price = soup0.find('div', class_='fl ack-ti').find('div', class_='nu').find('strong').text + '元'  # 起送价格
        send_price = soup0.find('div', class_='fl in-ti').find('div', class_='nu').find('strong').text + '元'  # 配送费
        menu = {}
        sale_time = soup0.find('div', class_='clearfix sale-time').find('span', class_='info-detail').text
        address = soup0.find('div', class_='rest-info-thirdpart poi-address').find('p', class_='poi-detail-right').text
        phone = soup0.find('div', class_='telephone').find('p', class_='poi-detail-right').text
        for category in soup0.find_all('div', class_='category'):
            category_name = category.find('h3')['title']
            menu[category_name] = []
            child = category.find('div')
            if child:
                for single_item in child.find_all('div', class_='j-pic-food'):
                    item_name = single_item.find('span', class_='name fl')['title']
                    item_zan = single_item.find('div', 'zan-count')
                    if item_zan:
                        item_zan = item_zan.text.strip().split(' ')[1]
                    else:
                        item_zan = '0'
                    item_price = single_item.find('div', 'only').text.strip()[1:]
                    item = {'name': item_name, 'zan': item_zan, 'price': item_price}
                    menu[category_name].append(item)
        html1 = requests.get(store_url1, headers=headers).text
        soup1 = BeautifulSoup(html1, 'html.parser')
        comment = soup1.find('div', class_='clearfix filters ct-deepgrey j-filters')
        comment_info = {}
        for span in comment.find_all('span'):
            comment_list = span.get_text().split(' ')
            comment_info[comment_list[0]] = comment_list[1][1:-1]
        print store_base[1], rank, avg_time, base_price, send_price, sale_time, address, phone
        info.append({
            'name': store_base[1],            # 店铺名
            'rank': rank,                     # 评分
            'avg_time': avg_time,             # 平均送达时间
            'base_price': base_price,         # 起送价
            'send_price': send_price,         # 配送费
            'menu': menu,                     # 菜单
            'comment_info': comment_info,     # 评论信息
            'address': address,               # 地址
            'sale_time': sale_time,           # 营业时间
            'phone': phone                    # 电话
        })
        time.sleep(15)
    with open('./store_data.json', 'w') as f:
        f.write(json.dumps(info, ensure_ascii=False))


if __name__ == '__main__':
    get_yaxin_waimai(headers)



