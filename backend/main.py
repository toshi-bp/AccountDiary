from flask import Flask, render_template, request, jsonify, redirect
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
jwt = JWTManager(app)
CORS(app, resources={r"/*": {"origins": "*"}})

# views読み込み
# app.register_blueprint(auth)

# ログインページにリダイレクトするための関数
@app.route('/')
def redirect_login():
    return redirect('http://localhost:5000/login')

# 認証部分
@app.route('/api/login', methods=['POST'])
def login():
    user = request.get_json()
    username = user['username']
    password = user['password']
    print("user:")
    print(user)
    if username == "" or password == "":
        return jsonify({"message": "Format does not match"}), 400
    try:
        result = get_user_by_name_and_pwd(username, password)
        print("result:")
        print(result)
        if not result:
            return jsonify({"message": "username or password is wrong"}), 401
    except:
        print("error")
        return jsonify( {"message": "An error occurred"} ), 500
    print("create toke")
    access_token = create_access_token(identity=result["id"])
    print(access_token)
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
    print(user)
    return jsonify(insert_user(user))

@app.route('/api/users/update', methods=['PUT'])
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
    image = request.get_json()
    # この段階でimageUrlの書き換えを行う
    code = base64.b64decode(image['image_url'].split(',')[1])
    image_decoded = Image.open(BytesIO(code))
    image_decoded.save('./uploads' + '/' + image['image_url'])
    return jsonify(insert_image(image))

@app.route('/api/images/update', methods=['PUT'])
def api_update_image():
    image = request.get_json()
    return jsonify(update_image(image))

@app.route('/api/images/delete/<user_id>', methods=['DELETE'])
def api_delete_image(user_id):
    return jsonify(delete_images(user_id))

# histories
@app.route('/api/histories', methods=['GET'])
def api_get_histories_status():
    return (get_histories())

@app.route('/api/histories/<user_id>', methods=['GET'])
def api_get_histories_by_id(user_id):
    return jsonify(get_histories_by_id(user_id))

@app.route('/api/histories/add', methods=['POST'])
def api_add_history():
    history = request.get_json()
    return jsonify(insert_history(history))

@app.route('/api/histories/update', methods=['PUT'])
def api_update_history():
    history = request.get_json()
    return jsonify(update_history(history))

@app.route('/api/histories/delete/<user_id>', methods=['DELETE'])
def api_delete_history(user_id):
    return jsonify(delete_histories(user_id))

@app.route('/api/categories', methods=['GET'])
def api_get_categories():
    return jsonify(get_categories())
# @app.route('/api/categories/<user_id>', methods=['GET'])
# def api_get_categories():
#     return jsonify(get_categories())

@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run()