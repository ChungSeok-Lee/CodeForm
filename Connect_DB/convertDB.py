from pymongo import MongoClient
import pymysql

#MongoDB 데이터 불러오기
client = MongoClient('mongodb://172.17.0.2:27017/')
mydb = client.mydb
ct_info = mydb.crawlingtask.find()

#MySQL 연결하기
conn = pymysql.connect(host='localhost', port =3306, user= 'scott', password='tiger', db='yojulabdb', charset='utf8', autocommit= True)
cursor = conn.cursor()
query = "INSERT INTO Economic (Title, Link) VALUES (%s, %s)"

for info in ct_info:
    if 'title' in info.keys():
        title = info['title']
        link = info['url']
        cursor.execute(query,(title, link))

conn.commit()
conn.close()