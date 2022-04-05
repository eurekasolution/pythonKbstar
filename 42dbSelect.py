#42dbSelect.py
from pymongo import MongoClient
import time
import os

try:
    client = MongoClient("mongodb://localhost:27017/")

    db = client['test']
    print('저자\t\t', '제목\t', '종류')
    for d in db['posts'].find():
         print(d['author'], '\t', d['title'], '\t', d['kind'])

    print('전체레코드갯수 =', db['posts'].estimated_document_count())
    print('전체레코드갯수 =', db['posts'].count_documents({}))
    print('=' * 100)
    print()

    name = input('저자검색입력 >>> ')
    search = db['posts'].count_documents( { 'author': name} )
    if search <= 0:
        print(name, "검색결과가 없습니다")
        exit(-1)

    result = db['posts'].find({'author': name})
    for d in result:
        print(d['author'], d['title'], d['kind'])

except Exception as err:
    print('db조회에러발생 : ', err)

