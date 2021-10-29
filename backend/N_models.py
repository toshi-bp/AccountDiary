from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# データベースの定義を行うモジュール
class User(db.Model):
    # テーブル名
    __tablename__ = 'user'

    # カラム情報
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    mail = db.Column(db.String(255), nullable=False)
    pwd = db.Column(db.String(255), nullable=False)
    birthday = db.Column(db.DateTime)
    gender = db.Column(db.String)
    phonenumber = db.Column(db.String(255))
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, mail, pwd, birthday, gender, phonenumber):
        self.name = name
        self.mail = mail
        self.pwd = pwd
        self.birthday = birthday
        self.gender = gender
        self.phonenumber = phonenumber

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'mail': self.mail,
            'pwd': self.pwd,
            'birthday': self.birthday,
            'phonenumber': self.phonenumber,
        }

class images(db.Model):
    # テーブル名
    __tablename__ = 'images'
    
    # カラム情報
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer)
    image_url = db.Column(db.String(255), nullable=False)
    act_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    diary = db.Column(db.String(255), nullable=False)

    def __init__(self, id, member_id, image_url, act_time, update_time, diary):
        self.id = id
        self.member_id = member_id
        self.image_url = image_url
        self.act_time = act_time
        self.update_time = update_time
        self.diary = diary
    
    # 抽象クラスを作成した方がわかりやすい...？

#メンバーシップに関するDB
class membership(db.Model):
    #テーブル名
    __tablename__ = 'membership'

    # カラム情報
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(255))
    pwd = db.Column(db.String(255), nullable=False)
    act_birthday = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(255), nullable=False)
    phonenumber = db.Column(db.String(255), nullable=False)

    def __init__(self, id, mail, pwd, birthday, gender, phonenumber):
        self.id = id
        self.mail = mail
        self.pwd = pwd
        self.act_birthday = birthday
        self.gender = gender
        self.phonenumber = phonenumber

class history(db.Model):
    #テーブル名
    __tablename__ = 'history'

    # カラム情報
    id = db.Column(db.Integer, primary_key=True)
    memberId = db.Column(db.Integer)
    action = db.Column(db.String(255), nullable=False)
    result = db.Column(db.Integer, nullable=False)
    act_time = db.Column(db.Date, nullable=False)
    update_time = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(255), nullable=False)

    def __init__(self, id, memberId, action, result, act_time, update_time,category):
        self.id = id
        self.memberId = memberId
        self.action= action
        self.result = result
        self.act_time = act_time
        self.update_time = update_time
        self.category = category

# default = datetime.now を使用するとわかりやすいかも


