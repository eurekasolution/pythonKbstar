#43dbSelectlike.py
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
    time.sleep(1)


    name2 = input('저자검색입력 like >>> ')
    search2 = db['posts'].count_documents( {'author': { '$regex':name2} })
    if search2 <= 0:
        print(name2, " like 검색결과가 없습니다")
        exit(-1)

    result = db['posts'].find({'author': { '$regex':name2} })
    for d in result:
        print(d['author'], d['title'], d['kind'])
    print('like 조회레코드갯수 =', db['posts'].count_documents({'author': { '$regex':name2} }))
except Exception as err:
    print('db조회에러발생 : ', err)

