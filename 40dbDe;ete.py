#40dbDelete.py
from pymongo import MongoClient
import time

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client['test']

    name = input('삭제데이터 저자 >>> ')
    #search = db['posts'].find( { 'author': name} )
    #delete_one()사용해서 삭제처리후 전체출력
    db['posts'].delete_one({'author': name})
    for d in db['posts'].find():
        print(d)
except Exception as err:
    print('db삭제에러발생 : ', err)

