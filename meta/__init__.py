from flask import Flask
from pymongo import MongoClient

# client = MongoClient('127.0.0.1', 27017)

# db = client.my_database #생성할 DB 이름
# db_accident = db.mycollection #생성하고자 하는 컬렉션 이름
# db_guardian = db.mycollection #생성하고자 하는 컬렉션 이름

def create_app():
    app = Flask(__name__)


    # app.config.from_pyfile('config.py')


    from .views import main_views, sms_views, wc_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(sms_views.bp)
    app.register_blueprint(wc_views.bp)



    return app
