import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbproject

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.post('https://korean.visitkorea.or.kr/call', headers=headers, data={'cmd': 'TOUR_CONTENT_LIST_VIEW',
                                                                                    'month': 'All',
                                                                                    'areaCode': 6,
                                                                                    'sigunguCode': 'All',
                                                                                    'tagId': 'All',
                                                                                    'sortkind': 3,
                                                                                    'locationx': 0,
                                                                                    'locationy': 0,
                                                                                    'page': 1,
                                                                                    'imgPath': 'All',
                                                                                    'cnt': 100,
                                                                                    'stampId': '1589345b-b030-11ea-b8bd-020027310001'})

places = data.json()['body']['result']
for place in places:
    newData = {
        'addr1': place['addr1'],
        'areaCode': place['areaCode'],
        'title': place['title'],
        'imgPath': place['imgPath']
    }
    db.places.update_one({'title': place['title']}, {'$set': {'imgPath': place['imgPath']}})