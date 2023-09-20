import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import Blueprint, jsonify, request, render_template
from .py_module import pymongo_db
from bson import json_util
import json

bp = Blueprint('main', __name__, url_prefix='/')

###기본화면####
@bp.route('/')
def index():
    return render_template('index.html')




#####DB 관련#######
@bp.route('/write')
def write():
    return render_template('write.html')


@bp.route('/insert_guardian')
def insert_guardian():
    pymongo_db.insert_guardian()
    return render_template('database_list.html')


@bp.route('/load_guardian')
def load_guardian():
    results = pymongo_db.load_guardian()
    return render_template('load_guardian.html', result=results)


@bp.route('/load_accident')
def load_accient():
    results = pymongo_db.load_accident()
    return render_template('load_accident.html', result=results)

@bp.route('/save_guardian')
def save_accident():
    insert_guardian('사용자','보호자','번호')
    results = pymongo_db.load_guardian()
    return render_template('load_guardian.html', result=results)






####비디오 게시판 내용#####
@bp.route('/video_list')
def video_list():
    return render_template('video_list.html')


@bp.route('/video_1')
def video_1():
    video_path = '/static/videos/test_1.mp4' 
    return render_template('video_show1.html', video_path=video_path)


@bp.route('/video_2')
def video_2():
    video_path = '/static/videos/test_2.mp4' 
    return render_template('video_show2.html', video_path=video_path)


@bp.route('/video_3')
def video_3():
    video_path = '/static/videos/test_3.mp4'
    return render_template('video_show3.html', video_path=video_path)


@bp.route('/video_4')
def video_4():
    video_path = '/static/videos/test_4.mp4'
    return render_template('video_show4.html', video_path=video_path)


@bp.route('/video_5')
def video_5():
    video_path = '/static/videos/test_5.mp4' 
    return render_template('video_show5.html', video_path=video_path)





# @bp.route('/accident_table', methods=['GET'])
# def accident_table_db():
#     print("이거 실행됨")
#     results = pymongo_db.load_accident()
#     #results = list(pymongo_db.load_accident())
#     print("result main_views:", results)
#     #return jsonify({'all_result': results})
#     return json.dumps({'all_result': results}, default=json_util.default)