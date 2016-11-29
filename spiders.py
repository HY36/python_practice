# -*- coding: utf-8 -*-

import requests, re
from bs4 import BeautifulSoup



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
        html = requests.get(url).text
        index_data = BeautifulSoup(html, "lxml")
        data = dict()
        name = index_data.select('div.info-box > h3')
        data['name'] = name.get_text().strip()
        abstracts = index_data.find_all("p", attrs={'class': "about"})
        for abstract in abstracts:
            data['abstract'] = abstract.get_text()
        ids = index_data.find_all("p", attrs={'class': "user_id"})
        for i in ids:
            data['id'] = i.get_text()
        print(data)



if __name__ == '__main__':
    url = 'http://www.huajiao.com/category/1000'
    liveId = getLiveId(url)
    userId = getUserId(liveId)
    getUserData(userId)