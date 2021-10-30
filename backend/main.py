from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from views.auth import *

# API設定
app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
jwt = JWTManager
CORS(app)

# views読み込み
app.register_blueprint(auth)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run()