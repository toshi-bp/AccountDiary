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

        for row in rows:
            # カラム情報を取得する
            user = {}
            user["id"] = row["id"]
            user["mail"] = row["mail"]
            user["password"] = row["password"]
            user["name"] = row["name"]
            user["birthday"] = row["birthday"]
            user["gender"] = row["gender"]
            user["phonenumber"] = row["phonenumber"]
            user["money"] = row["money"]
            user["used_money"] = row["used_money"]
            user["jti"] = row["jti"]
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
        cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cur.fetchone()
        print("row:")
        print(row)

        # 辞書型に変換
        user["id"] = row["id"]
        user["mail"] = row["mail"]
        user["password"] = row["password"]
        user["name"] = row["name"]
        user["birthday"] = row["birthday"]
        user["gender"] = row["gender"]
        user["phonenumber"] = row["phonenumber"]
        user["money"] = row["money"]
        user["used_money"] = row["used_money"]
        user["jti"] = row["jti"]
    except:
        print("error")
        user = {}
    print("user:")
    print(user)
    return user

# 認証に利用
def get_user_by_name_and_pwd(username, password):
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE name = ? AND password = ?", (username, password))
        row = cur.fetchone()

        # 辞書型に変換
        user["id"] = row["id"]
        user["mail"] = row["mail"]
        user["password"] = row["password"]
        user["name"] = row["name"]
        user["birthday"] = row["birthday"]
        user["gender"] = row["gender"]
        user["phonenumber"] = row["phonenumber"]
        user["money"] = row["money"]
        user["used_money"] = row["used_money"]
        user["jti"] = row["jti"]
    except:
        user = {}
    return user

def get_images():
    images = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM images")
        rows = cur.fetchall()

        for row in rows:
            image = {}
            image["id"] = row["id"]
            image["user_id"] = row["user_id"]
            image["image_url"] = row["image_url"]
            image["act_time"] = row["act_time"]
            image["update_time"] = row["update_time"]
            image["update_time"] = row["update_time"]
            image["diary"] = row["diary"]
            image["score"] = row["score"]
            images.append(image)
    except:
        images = []
    return images

def get_images_by_id(user_id):
    images = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM images WHERE user_id = ?", (user_id,))
        rows = cur.fetchall()

        for row in rows:
            image = {}
            image["id"] = row["id"]
            image["user_id"] = row["user_id"]
            image["image_url"] = row["image_url"]
            image["act_time"] = row["act_time"]
            image["update_time"] = row["update_time"]
            image["update_time"] = row["update_time"]
            image["diary"] = row["diary"]
            image["score"] = row["score"]
            images.append(image)
    except:
        images = []
    return images

def get_histories():
    histories = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM histories")
        rows = cur.fetchall()

        for row in rows:
            # カラム情報を取得する
            history = {}
            history["id"] = row["id"]
            history["user_id"] = row["user_id"]
            history["action"] = row["action"]
            history["result"] = row["result"]
            history["act_time"] = row["act_time"]
            history["update_time"] = row["update_time"]
            history["category"] = row["category"]
            histories.append(history)
    except:
        histories = []
    return histories

def get_histories_by_id(user_id):
    histories = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM histories WHERE user_id = ?", (user_id,))
        rows = cur.fetchall()

        for row in rows:
            # カラム情報を取得する
            history = {}
            history["id"] = row["id"]
            history["user_id"] = row["user_id"]
            history["action"] = row["action"]
            history["result"] = row["result"]
            history["act_time"] = row["act_time"]
            history["update_time"] = row["update_time"]
            history["category"] = row["category"]
            histories.append(history)
    except:
        histories = []
    return histories

def get_categories():
    categories = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM categories")
        rows = cur.fetchall()

        for row in rows:
            # カラム情報を取得する
            category = {}
            category["id"] = row["id"]
            category["user_id"] = row["user_id"]
            category["type"] = row["type"]
            category["category"] = row["category"]
            categories.append(category)
    except:
        categories = []
    return categories

def get_categories_by_id(user_id):
    categories = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM categories  WHERE user_id = ?", (user_id, ))
        rows = cur.fetchall()

        for row in rows:
            # カラム情報を取得する
            category = {}
            category["id"] = row["id"]
            category["user_id"] = row["user_id"]
            category["type"] = row["type"]
            category["category"] = row["category"]
            categories.append(category)
    except:
        categories = []
    return categories