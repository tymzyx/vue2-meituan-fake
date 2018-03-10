# -*- coding:utf-8
import requests
from bs4 import BeautifulSoup  # 解析网页
import json

url = 'http://bj.meituan.com/'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'bj.meituan.com',
    'Referer': 'http://www.meituan.com/',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Content-Type': 'text/html; charset=utf-8'
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
    html = requests.get(url, headers = headers).text
    soup = BeautifulSoup(html, 'html.parser')
    content_id = 1


if __name__ == '__main__':
    get_home(url)



