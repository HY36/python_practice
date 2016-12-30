# -*- coding: utf-8 -*-

import requests, re
from bs4 import BeautifulSoup

headers = {
            "Accept-Encoding":"gzip",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Referer":"http://www.example.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
            }


def getLiveId(url):

    html = requests.get(url, headers=headers).text

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

    for i in userId:
        url = "http://www.huajiao.com" + str(i)
        html = requests.get(url, headers=headers).text
        index_data = BeautifulSoup(html, "lxml")
        data = dict()
        data['url'] = url
        name = index_data.h3
        data['name'] = name.get_text().strip()
        abstracts = index_data.find_all("p", attrs={'class':"about"})
        for abstract in abstracts:
            data['abstract'] = abstract.get_text()
        ids = index_data.find_all("p", "user_id")
        for i in ids:
            data['id'] = i.get_text()
        print(data)



if __name__ == '__main__':
    url = 'http://www.huajiao.com/category/1000'
    liveId = getLiveId(url)
    userId = getUserId(liveId)
    getUserData(userId)