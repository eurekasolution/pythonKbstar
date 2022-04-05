#39dbSelect.py
from pymongo import MongoClient
import time

try:
    client = MongoClient("mongodb://localhost:27017/")

    db = client['test']
    print('저자\t\t', '제목\t', '종류')
    print('=' * 50)
    for d in db['posts'].find():
         print(d['author'], '\t', d['title'], '\t', d['kind'])

    print('전체레코드갯수 =', db['posts'].estimated_document_count())
except Exception as err:
    print('db조회에러발생 : ', err)