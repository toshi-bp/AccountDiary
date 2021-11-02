from flask import Flask, render_template, request, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from views.auth import *

from database.get_data import *
from database.insert import *
from database.update import *
from database.delete import *

# API設定
app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
jwt = JWTManager
CORS(app, resources={r"/*": {"origins": "*"}})

# views読み込み
app.register_blueprint(auth)

@app.route('/', defaults={'path': ''})

# users
@app.route('/api/users', methods=['GET'])
def api_get_status():
    return jsonify(get_users())

@app.route('/api/users/<user_id>', methods=['GET'])
def api_get_user(user_id):
    return jsonify(get_user_by_id(user_id))

@app.route('/api/users/add', methods=['POST'])
def api_add_user():
    user = request.get_json()
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

@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run()