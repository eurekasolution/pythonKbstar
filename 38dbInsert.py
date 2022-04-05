#38dbInsert.py
from pymongo import MongoClient
import time

try:
    client = MongoClient("mongodb://localhost:27017/")
    print(client.list_database_names()) #admin,config,local
    print()

    db = client['test'] #데이터베이스생성
    print('test데이터베이스 생성 success 11:34')
    data = {
        'author' : 'kim' ,
        'title' : 'apple' ,
        'kind' : 'red'
    }
    db.posts.insert_one(data) #db.테이블명=Collection
    print('데이터 한건 성공 ')
    print('-' * 100)
except Exception as err:
    print('db에러발생 : ', err)