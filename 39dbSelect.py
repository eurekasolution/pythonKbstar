#39dbSelect.py
from pymongo import MongoClient
import time

try:
    client = MongoClient("mongodb://localhost:27017/")

    db = client['test']
    print('저자', '제목', '종류')
    print('=' * 50)
    for d in db['posts'].find(): #find()함수=select * from 테이블명
         print(d['author'], d['title'], d['kind'])
except Exception as err:
    print('db조회에러발생 : ', err)