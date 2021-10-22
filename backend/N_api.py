from flask import Blueprint, request, abort, jsonify

from models import db, User, images

# api Blueprint作成
api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/mypage', method=['POST'])
def post_user():
    # jsonリクエストから値取得
    payload = request.json
    name = payload.get('name')
    mail = payload.get('mail')
    pwd = payload.get('pwd')
    birthday = payload.get('birthday')
    gender = payload.get('gender')
    phonenumber = payload.get('phonenumber')
    
    # レコードの登録 新規作成したオブジェクトをaddしてcommit
    user = User(name, mail, pwd, birthday, gender, phonenumber)
    db.session.add(user)
    db.session.commit()

    response = jsonify(user.to_dict)
    # レスポンスヘッダ設定
    response.headers['Location'] = '/api/users/%d' % user.id
    # HTTPステータスを200以外で返却したい場合
    return response, 201
