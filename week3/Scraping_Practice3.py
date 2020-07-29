import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
table = soup.select('#regularTeamRecordList_table > tr')

for team_rank in table:
    rank = team_rank.select_one('th > strong').text
    team_name = team_rank.select_one('td.tm > div > span').text
    win_rate = team_rank.select_one('td:nth-child(7) > strong').text

    if float(win_rate) > 0.5:
        print(rank, team_name, win_rate)
