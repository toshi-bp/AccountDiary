from flask import Flask, render_template, request, jsonify, redirect, send_from_directory, url_for
from flask_jwt_extended import JWTManager, create_access_token
from flask_cors import CORS

import base64
from PIL import Image
from io import BytesIO
from pathlib import Path

from get_data import *
from insert import *
from update import *
from delete import *

# API設定
app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app.config['SECRET_KEY'] = 'secret'
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
jwt = JWTManager(app)
CORS(app, resources={r"/*": {"origins": "*"}})

# views読み込み
# app.register_blueprint(auth)

# ログインページにリダイレクトするための関数
@app.route('/')
def redirect_login():
    # return redirect('http://localhost:5000/login)
    return redirect('https://nikkidekakeibo.azurewebsites.net/login')

# 認証部分
@app.route('/api/login', methods=['POST'])
def login():
    user = request.get_json()
    username = user['username']
    password = user['password']
    if username == "" or password == "":
        return jsonify({"message": "Format does not match"}), 400
    try:
        result = get_user_by_name_and_pwd(username, password)
        if not result:
            return jsonify({"message": "username or password is wrong"}), 401
    except:
        return jsonify( {"message": "An error occurred"} ), 500
    access_token = create_access_token(identity=result["id"])
    update_user_jti(result, access_token)
    return jsonify(access_token=access_token, user_id=result["id"]), 200

# users
@app.route('/api/users', methods=['GET'])
def api_get_status():
    return jsonify(get_users())

@app.route('/api/users/<user_id>', methods=['GET'])
def api_get_user(user_id):
    return jsonify(get_user_by_id(user_id))

# 新規登録の際に利用
@app.route('/api/users/add', methods=['POST'])
def api_add_user():
    user = request.get_json()
    return jsonify(insert_user(user))

@app.route('/api/users/update', methods=['POST'])
def api_update_user():
    user = request.get_json()
    return jsonify(update_user(user))

@app.route('/api/users/delete/<user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    return jsonify(delete_user(user_id))

# images
@app.route('/api/images', methods=['GET'])
def api_get_images_status():
    return jsonify(get_images())

@app.route('/api/images/<user_id>', methods=['GET'])
def api_get_images_by_id(user_id):
    return jsonify(get_images_by_id(user_id))

@app.route('/api/images/add', methods=['POST'])
def api_add_image():
    # この段階でimageUrlの書き換えを行う
    image = request.get_json()
    code = base64.b64decode(image['image_url'].split(',')[1])
    image_decoded = Image.open(BytesIO(code))
    image_decoded.save(Path(app.config['UPLOAD_FOLDER']) / image['file_name'])
    image["image_url"] = url_for('uploaded_image', file_name=image["file_name"])
    return jsonify(insert_image(image))

@app.route('/api/images/update', methods=['POST'])
def api_update_image():
    image = request.get_json()
    return jsonify(update_image(image))

@app.route('/api/images/delete/<user_id>', methods=['DELETE'])
def api_delete_image(user_id):
    return jsonify(delete_images(user_id))

# histories
@app.route('/api/histories', methods=['GET'])
def api_get_histories_status():
    return jsonify(get_histories())

@app.route('/api/histories/<user_id>', methods=['GET'])
def api_get_histories_by_id(user_id):
    return jsonify(get_histories_by_id(user_id))

@app.route('/api/histories/add', methods=['POST'])
def api_add_history():
    history = request.get_json()
    return jsonify(insert_history(history))

@app.route('/api/histories/update', methods=['POST'])
def api_update_histories_category():
    history = request.get_json()
    return jsonify(update_hisotries_category(history))

@app.route('/api/histories/delete/<user_id>', methods=['DELETE'])
def api_delete_history(user_id):
    return jsonify(delete_histories(user_id))

# categories
@app.route('/api/categories', methods=['GET'])
def api_get_categories_status():
    return jsonify(get_categories())

@app.route('/api/categories/<user_id>', methods=['GET'])
def api_get_categories_by_id(user_id):
    return jsonify(get_categories_by_id(user_id))

@app.route('/api/categories/add', methods=['POST'])
def api_add_category():
    category = request.get_json()
    print("new category")
    print(category)
    return jsonify(insert_category(category))

@app.route('/api/categories/delete/<user_id>', methods=['DELETE'])
def api_delete_category(user_id):
    return jsonify(delete_categories(user_id))

##パスワードのアップデート
@app.route('/api/users/update_pass/<user_id>', methods=['PATCH'])
def api_update_user_pwd(user_id):
    re = request.get_json()
    user_id = re["user_id"]
    password = re["password"]
    return jsonify(update_user_pwd(user_id, password))

#予算のアップデート
@app.route('/api/users/update_money/<user_id>', methods=['PATCH'])
def api_update_user_money(user_id):
    re = request.get_json()
    print(re)
    user_id = re["user_id"]
    money = re["money"]
    type = re["type"]
    return jsonify(update_user_money(user_id, money, type))

# アップロードされた画像の表示に利用
@app.route('/images/<file_name>')
def uploaded_image(file_name):
    # 画像urlはBASE_URL + /images/<file_name>
    return send_from_directory(app.config['UPLOAD_FOLDER'], file_name)

# #カテゴリのアップデート→なし
# @app.route('/api/histories/update', methods=['POST'])
# def api_update_hisotries_category():
#     history = request.get_json()
#     return jsonify(api_update_hisotries_category(history))

@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run()