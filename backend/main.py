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

@app.route('/api/users', methods=['GET'])
def api_get_status():
    return jsonify(get_users())

@app.route('/api/users/<user_id>', methods=['GET'])
def api_get_user(user_id):
    return jsonify(get_user_by_id(user_id))

@app.route('/api/users/add', methods=['POST'])
def api_add_user():
    user = request.get_json()
    return jsonify(update_user(user))

@app.route('/api/users/update', methods=['PUT'])
def api_update_user():
    user = request.get_json()
    return jsonify(update_user(user))

@app.route('/api/users/delete/<user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    return jsonify(delete_user(user_id))

@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run()