#40dbDelete.py
from pymongo import MongoClient
import time

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client['test']

    name = input('삭제데이터 저자 >>> ')
    search = db['posts'].find_one({'author': name})
    if search is None:
        print(name, "삭제관련검색결과가 없습니다")
        exit(-1)

    db['posts'].delete_one({'author': name})
    print('삭제처리후 데이터확인')

    time.sleep(1)
    for d in db['posts'].find():
        print(d)
except Exception as err:
    print('db삭제에러발생 : ', err)

