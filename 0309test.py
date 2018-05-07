import unittest
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib import parse
# import pymongo
import time
import requests
import random

youxii=0
youxij=0
youxinum=0

movie_name = '倚天屠龙记'
# print('正在查找第{}个电影:'.format(youxii) + movie_name)
movie_name_utf = movie_name.encode("UTF-8")
url = 'https://newgame.17173.com/game-search.html?keyword=' + parse.quote(movie_name_utf)
print (url)
try:
    html = requests.get(url,timeout=120,proxies='http://117.90.6.84 9000')
    time.sleep(1)
    soup = BeautifulSoup(html.text, 'lxml')
    result = soup.find('div', {'class': 'content-ex'})
    num = result.div.get('class')
    if num[0] != 'box-result-none':
        # pnbds = result.find_all('div', {'class': 'pn-bd'})
        # for pndb in pnbds:
        #     items = pndb.find_all('li')
        items = result.find_all('li',limit = 5)
        for item in items:
            youxinum=youxinum+1
            href = 'http://newgame.17173.com' + item.a.get('href')
            details = item.find_all('span')
            img = details[0].img.get('src')
            name = details[0].img.get('alt')
            data={
                'movie_name':movie_name,
                'name':name,
                'href':href,
                'img_link':img
            }
            print(data)
            # game.insert_one(data)
            print (name)
            print (href)
            print (img)
    else:
        youxij=youxij+1
        print('******' + movie_name + '******无结果')
except AttributeError:
    youxij = youxij + 1
    print('******' + movie_name + '******异常无结果')
    pass




# for movie in movie_profile.find({},{'name':1,'_id':0}):
#     time.sleep(1)
#     youxii = youxii + 1
#
#
#     try:
#         html = requests.get(url,timeout=120,proxies='http://117.90.6.84 9000')
#         time.sleep(1)
#         soup = BeautifulSoup(html.text, 'lxml')
#         result = soup.find('div', {'class': 'content-ex'})
#         num = result.div.get('class')
#         if num[0] != 'box-result-none':
#             # pnbds = result.find_all('div', {'class': 'pn-bd'})
#             # for pndb in pnbds:
#             #     items = pndb.find_all('li')
#             items = result.find_all('li',limit = 5)
#             for item in items:
#                 youxinum=youxinum+1
#                 href = 'http://newgame.17173.com' + item.a.get('href')
#                 details = item.find_all('span')
#                 img = details[0].img.get('src')
#                 name = details[0].img.get('alt')
#                 data={
#                     'movie_name':movie_name,
#                     'name':name,
#                     'href':href,
#                     'img_link':img
#                 }
#                 game.insert_one(data)
#                 # print (name)
#                 # print (href)
#                 # print (img)
#         else:
#             youxij=youxij+1
#             print('******' + movie_name + '******无结果')
#     except AttributeError:
#         youxij = youxij + 1
#         print('******' + movie_name + '******异常无结果')
#         pass
# print('******共查找{}个电影******'.format(youxii))
# print('******共有{}个电影无结果******'.format(youxij))
# print('******共有{}条游戏******'.format(youxinum))
