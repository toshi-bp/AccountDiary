############使用しないです。










from pyexpat import model
from statistics import mode
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# DBに直接的な接続の情報を格納

#####パスの指定
database_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'AccountDiary.db')

#####パスを用いて、エンジンを作成
engine = create_engine('sqlite:///' + database_file, convert_unicode=True)
#engine = create_engine('sqlite://root:localhost@localhost/foo' )

#####dbのsession開始
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

#####モデルデータベースクラスの作成
Model = declarative_base(bind=engine)

db = AccountDiary.db

######追加したもの
class User(Model):
    # テーブル名
    __tablename__ = 'user'

    # カラム情報
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    mail = Column(String(255), nullable=False)
    pwd = Column(String(255), nullable=False)

###コメントアウトしました###
# def init_db():
#     import models
    
#     Model.metadata.create_all(bind=engine)

#####Modelを引数に持つテーブルをDBに作成する。
Model.metadata.create_all(engine)
#Model.metadata.create_all(engine)
#Model.query = db_session.query_property()

#####セッションの作成
SessionClass = sessionmaker(engine)
session = SessionClass()

#####お試しでデータを入れてみたい。
user_a = User(id = "5", name ="rikadai", mail ="@ed.tus", pwd ="TUS")
session.add(user_a)
session.commit()

#####
users = session.query(User).all() 
print(users)