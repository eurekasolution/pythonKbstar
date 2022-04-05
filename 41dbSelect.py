#41dbSelect.py
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
    print('=' * 100)
    print()

    name = input('저자검색입력 >>> ')
    search = db['posts'].find({'author': name })
    count = len(list(search))
    print('조회갯수 =', count)

    if count <= 0:
        print(name, "검색결과가 없습니다")
        exit(-1)

    for d in search:
        print(d['author'], d['title'], d['kind'])

    print('41dbSelect.py 마지막문서입니다')
except Exception as err:
    print('db조회에러발생 : ', err)

