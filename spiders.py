# -*- coding: utf-8 -*-

import requests, re
from bs4 import BeautifulSoup
from lxml import etree


headers = { 'Host':'www.super-ping.com',
                    'Connection':'keep-alive',
                    'Cache-Control':'max-age=0',
                    'Accept': 'text/html, */*; q=0.01',
                    'X-Requested-With': 'XMLHttpRequest',
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
                    'DNT':'1',
                    'Referer': 'http://www.super-ping.com/?ping=www.google.com&locale=sc',
                    'Accept-Encoding': 'gzip, deflate, sdch',
                    'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'
                    }

def getLiveId(url):

    html = requests.get(url).text

    index_data = BeautifulSoup(html, "lxml")

    live_id = index_data.find_all("a", href=re.compile(r'^(/l/)'))
    liveId = []
    for i in live_id:
        if 'href' in i.attrs:
            liveId.append(i['href'])

    return liveId

def getUserId(liveId):

    userId = []

    for i in liveId:
        url = "http://www.huajiao.com" + str(i)
        html = requests.get(url).text
        index_data = BeautifulSoup(html, "lxml")
        user_id = index_data.find_all("a", attrs={"class": "link"}, href=re.compile(r'^(/user/)'))
        for i in user_id:
            if 'href' in i.attrs:
                userId.append(i['href'])
    return set(userId)

def getUserData(userId):

    for i in liveId:
        url = "http://www.huajiao.com" + str(i)
        html = requests.post(url, headers=headers).text
        # index_data = BeautifulSoup(html,  ["lxml", "xml"])
        # print(index_data)
        tree = etree.HTML(html)
        data = dict()
        # names = index_data.find_all("h3")
        # data['name'] = names[0].get_text().strip()
        # abstracts = index_data.find_all("div", attrs={'class':"info-box"})
        # for abstract in abstracts:
        #     data['abstract'] = abstract.get_text()
        # ids = index_data.find_all("p", "user_id")
        # for i in ids:
        #     data['id'] = i.get_text()
        abstracts = tree.xpath('//p[@class="about"]/text()')
        print(abstracts)



if __name__ == '__main__':
    url = 'http://www.huajiao.com/category/1000'
    liveId = getLiveId(url)
    userId = getUserId(liveId)
    getUserData(userId)