from bs4 import BeautifulSoup
from pprint import pprint
import requests

html = requests.get('https://search.daum.net/search?w=tot&DA=Z8T&q=%EC%88%98%EC%9B%90%EC%8B%9C%20%EC%9E%A5%EC%95%88%EA%B5%AC%20%EC%A1%B0%EC%9B%902%EB%8F%99%20%EB%82%A0%EC%94%A8&rtmaxcoll=Z8T')

soup = BeautifulSoup(html.text, 'html.parser')

data1 = soup.find('div', {'class': 'desc_temp'})

find_currenttemp = data1.find('strong',{'class': 'highest'}).text
current = soup.select('#weatherColl > div.coll_cont > div > div.wrap_tbl.week > table.tbl_calendar.hide > tbody > tr:nth-child(2) > td.today > div > strong.highest').text
print('현재 온도: '+current+'℃')

# data2 = data1.findAll('dd')
# find_dust = data2[0].find('span', {'class':'num'}).text
# find_ultra_dust = data2[1].find('span', {'class':'num'}).text
# find_ozone = data2[2].find('span', {'class':'num'}).text
# print('현재 미세먼지: '+find_dust)
# print('현재 초미세먼지: '+find_ultra_dust)
# print('현재 오존지수: '+find_ozone)


#weatherColl > div.coll_cont > div > div.wrap_tbl.week > table.tbl_calendar.hide > tbody > tr:nth-child(2) > td:nth-child(4) > div > strong.highest
#weatherColl > div.coll_cont > div > div.wrap_tbl.week > table.tbl_calendar.hide > tbody > tr:nth-child(2) > td:nth-child(6) > div > strong.highest