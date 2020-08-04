from pymongo import MongoClient

#Docker로 띄운 원격 Mongodb server로 접속
client = MongoClient('mongodb://172.17.0.2:27017/') #cmd로 띄운 docker_mongodb의 IP & Port Num
mydb = client.mydb # get Database

# 단일 insert 문 _ dict 형태
# board_info = mydb.board.insert_one(dict{})

# 다중 insert 문 _ list 형태
data = [
    {'name': "Lee", "age":"26", "city":"Hyderabad"},
    {'name': "Rahim", "age":"27", "city":"Seoul"}
]
res = mydb.board.insert_many(data)
print("Data inserted ..", res.inserted_ids) #insert된 data 확인

#db 상의 데이터 확인
board_info = mydb.board.find()
for info in board_info:
    print(info)

