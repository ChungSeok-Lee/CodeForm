from background_task import background
import time
import requests
from bs4 import BeautifulSoup as bs
import sqlite3

# --예시--#
# @background()
# def task_hello(schedule= 10, repeat=60):
#     time_tuple = time.localtime()
#     time_str = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
#     print("task ...Hello World!", time_str)

# django.setting.py 중 INSTALLED_APPS에 'background_task' 추가
# urls에서 함수 import하고 최하단에 함수 기입
# python manage.py process_tasks

# schedule setting
    # f(schedule= 90) __ 90seconds from now
    # f(schedule= timedelta(minutes=20))  __ 20 mins from now
    # f(schedule= timezone.now()) at specific time 


@background()
def task_crawling_daum(schedule= 10, repeat=60):
    conn = sqlite3.connect('db.sqlite3')
    query = 'CREATE TABLE economic (title TEXT, link TEXT)'
    conn.execute(query)
    conn.commit
    conn.close()
    res = requests.get('http://media.daum.net/economic/')
    if res.status_code == 200:
        soup = bs(res.content, 'html.parser')
        links = soup.find_all('a', class_ = 'link_txt')
        with sqlite3.connect("db.sqlite3") as con:
            cur = con.cursor()
            title = str()
            link = str()
            for link in links:
                title = str.strip(link.get_text())
                link = link.get('herf')
                cur.execute("INSERT INTO economic (title, link) VALUES (?,?)",(title, link))
                con.commit()
                time_tuple = time.localtime()
                time_str = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
                print("task ...Hello World!", time_str)