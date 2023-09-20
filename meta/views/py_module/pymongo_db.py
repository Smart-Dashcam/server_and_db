from pymongo import MongoClient
import datetime as dt
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#from __init__ import db_accident, db_guardian

client = MongoClient('127.0.0.1', 27017)# 127.0.0.1 => 몽고디비 IP / 27017 => 포트번호

db = client.smart_dashcam #생성할 DB 이름
db_accident = db.accident #생성하고자 하는 컬렉션 이름
db_guardian = db.guardian #생성하고자 하는 컬렉션 이름
#test
# db = client.my_database #생성할 DB 이름
# db_accident = db.my_collection #생성하고자 하는 컬렉션 이름
# db_guardian = db.my_collection #생성하고자 하는 컬렉션 이름

###############사고 관련 DB
#데이터 삭제
def delete_accident(name):
    db_accident.delete_one({"name": name})  # 가장 먼저 검색되는 것만 삭제
    #collection.delete_many({class_name: name})  # 이에 해당하는 거 모두 삭제
    print(name+"님의 정보 삭제")


#데이터 수정 및 추가하기
def change_accident(name):
    db_accident.update_one({"name": "홍길동"}, {'$set': {"bio": "한국인입니다."}}, upsert=True)#가장 먼저 있는 거 수정, upset-> 없으면 추가
    #다중 수정
    #collection.update_many({"bio" : "한국인입니다."}, {'$set': {"age" : 20}}, upsert=True)
    print(name+"님의 정보 수정 완료")


#데이터 불러오기
def load_accident():
    allData = db_accident.find()
    result = []
    for temp in allData:
        result.append(temp)
    return result


#데이터 입력
def insert_accident(name, lat, lng):
    dt_time = dt.datetime.now()
    document = {"name": name,
                "date": str(dt_time.year)+'-'+str(dt_time.month)+'-'+str(dt_time.day),
                "time": str(dt_time.hour)+'-'+str(dt_time.minute)+'-'+str(dt_time.second),
                "lat": lat,#위도
                "lng": lng} #경도
    #도큐먼트 하나 넣기
    db_accident.insert_one(document)
    print("사고 내용 - DB 입력 완료")
    #도큐먼트 여러개 한방에 넣기
    #L = [document1, document2] #리스트에 여러 개의 도큐먼트를 넣어줍니다.
    #collection.insert_many(L)





################보호자 관련 DB
#데이터 삭제
def delete_guardian(name):
    db_guardian.delete_one({"name": name})  # 가장 먼저 검색되는 것만 삭제
    #collection.delete_many({class_name: name})  # 이에 해당하는 거 모두 삭제
    print(name+"님의 정보 삭제")


#데이터 수정 및 추가하기
def change_guardian(name):
    db_guardian.update_one({"name": ""}, {'$set': {"bio": ""}}, upsert=True)#가장 먼저 있는 거 수정, upset-> 없으면 추가
    #다중 수정
    #collection.update_many({"bio" : "한국인입니다."}, {'$set': {"age" : 20}}, upsert=True)
    print(name+"님의 정보 수정 완료")
1

#데이터 불러오기
def load_guardian():
    allData = db_guardian.find()
    result = []
    for temp in allData:
        result.append(temp)
    print("보호자 정보 전송 완료")
    return result


def insert_guardian(name, guardian_name, guardian_number):
    document = {"name": name,
                "guardian_name": guardian_name,
                "guardian_number": str(guardian_number)}
    #도큐먼트 하나 넣기
    db_guardian.insert_one(document)
    print(name+"님의 보호자 입력 완료")



#flask run --host=0.0.0.0 --port=5000