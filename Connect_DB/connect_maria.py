import pymysql

#MySQL 연결하기
db = pymysql.connect(host='localhost', port =3306, user= 'scott', password='tiger', db='yojulabdb', charset='utf8', autocommit= True)
cursor = db.cursor(pymysql.cursors.DictCursor)
cursor.execute("SELECT * FROM Economic")
data = cursor.fetchall()
for infor in data:
    print("Economic: %s" % infor['Title'])

db.close()