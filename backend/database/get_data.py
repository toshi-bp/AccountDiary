import sqlite3
import sqlite3
from create_db import connect_to_db

def get_users():
    users = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()

        for i in rows:
            # カラム情報を取得する
            user = {}
            user["id"] = i["id"]
            user["mail"] = i["mail"]
            user["password"] = i["password"]
            user["name"] = i["name"]
            user["birthday"] = i["birthday"]
            user["gender"] = i["gender"]
            user["phonenumber"] = i["phonenumber"]
            users.append(user)
    except:
        users = []
    return users

def get_user_by_id(user_id):
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id))
        row = cur.fetchone()

        # 辞書型に変換
        user["id"] = row["id"]
        user["mail"] = row["mail"]
        user["password"] = row["password"]
        user["name"] = row["name"]
        user["birthday"] = row["birthday"]
        user["gender"] = row["gender"]
        user["phonenumber"] = row["phonenumber"]
    except:
        user = {}
    return user

def get_images():
    return

def get_images_by_id(user_id):
    images = []
    return

def get_histories():
    return

def get_histories_by_id(user_id):
    images = []
    return