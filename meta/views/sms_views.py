from flask import Blueprint
from .py_module.ncloudsms import sendmsg
from .py_module.gps import get_gps
import json
from .py_module.pymongo_db import insert_accident, load_guardian

bp = Blueprint('sms', __name__, url_prefix='/sms')


@bp.route('/')
def sms_route():
    return "sms default page"


@bp.route('/send')
def sms_send(name='사용자'):

    number = []
    # gps 위도 경도 불러오기
    lat, lng = get_gps()
    insert_accident(name, lat, lng)
    result = load_guardian()
    #보호자들 번호만 저장
    for i, temp in enumerate(result):
        number.append(temp['guardian_number'])
    print("전송하는 보호자 번호 :",number)

    for num in number:
        # 공백 제외 최대 80바이트
        response_text = sendmsg(int(num), content=name +
                                f"님의 사고가 감지되었습니다. 위치: [{lat}, {lng}] 기존에 저장된 연락처로 전송함.")

        response_json = json.loads(response_text)


    # 메세지 전송 성공여부
    if "202" in response_json["statusCode"]:
        insert_accident(name, lat, lng)
        return "success"
    else:
        return "fail"    
    ##flask run --host=0.0.0.0 --port=5000

    