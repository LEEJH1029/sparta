import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
tr_list = soup.select('#old_content > table > tbody > tr')

for tr in tr_list:
    title_tag = tr.select_one('td.title > div > a')
    rank_img = tr.select_one('td:nth-child(1) > img')
    point_tag = tr.select_one('td.point')

    if title_tag is not None:
        title = title_tag.text
        rank = rank_img['alt']
        point = point_tag.text
        print(rank, title, point)
