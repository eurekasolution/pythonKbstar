#39dbSelect.py
from pymongo import MongoClient
import time
import os

try:
    client = MongoClient("mongodb://localhost:27017/")

    db = client['test']
    print('저자\t\t', '제목\t', '종류')
    print('=' * 50)
    for d in db['posts'].find():
         print(d['author'], '\t', d['title'], '\t', d['kind'])

    print('전체레코드갯수 =', db['posts'].estimated_document_count())
    print()
    name = input('저자검색입력 >>> ') #select * from T where author='two' ;
    search = db['posts'].find( { 'author': name} )
    # print('search 값 ' , search )
    if search is None:
        print(name, ' 검색결과가 없습니다')
        exit(-1)

    print(name, ' 검색결과로 아래데이터 출력성공')
    for d in search:
        print(d['author'], d['title'], d['kind'])

    print('저자 like조건으로 검색하기 ')
    time.sleep(2)
    name2 = input('저자검색입력 like >>> ') #~~T where author like '%t%' ;
    search2 = db['posts'].find({'author': { '$regex':name2} })
    for d2 in search2:
        print(d2['author'], d2['title'], d2['kind'])
except Exception as err:
    print('db조회에러발생 : ', err)

