from create_db import connect_to_db
from get_data import *
import base64
from PIL import Image
from io import BytesIO
from pathlib import Path

# ユーザー情報を挿入するための関数
def insert_user(user):
    inserted_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users(id, mail, password, name, birthday, gender, phonenumber, money, used_money, jti) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (user['id'], user['mail'], user['password'], user['name'], user['birthday'], user['gender'], user['phone'], user['money'], user["used_money"], user['jti']))
        conn.commit()
        inserted_user = get_user_by_id(cur.lastrowid)
    except:
        print("no data")
        conn().rollback()
    finally:
        conn.close()
    return inserted_user

def insert_image(image):
    inserted_image = {}
    # この段階でimageUrlの書き換えを行う
    code = base64.b64decode(image['image_url'].split(',')[1])
    image_decoded = Image.open(BytesIO(code))
    image_decoded.save('./uploads' + '/' + image['image_url'])
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO images(user_id, image_url, act_time, update_time, diary, score) VALUES(?, ?, ?, ?, ?, ?)",
            (image['user_id'], image['image_url'], image['act_time'], image['update_time'], image['diary'], image['score'])
        )
        conn.commit()
        # TODO:返り値がただ一つになるようにidとdiary or image_urlでデータを絞るようにする
        inserted_image = get_images_by_id(cur.lastrowid)
    except:
        conn().rollback()
    finally:
        conn.close()
    return inserted_image

def insert_history(history):
    inserted_history = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO histories(user_id, action, result, act_time, update_time, type, category, place) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
            (history['user_id'], history['action'], history['result'], history['act_time'], history['update_time'], history['type'], history['category'],history['place'])
        )
        conn.commit()
        inserted_history = get_histories_by_id_and_diary(history["user_id"], history["action"])
        print(inserted_history)
    except:
        conn().rollback()
    finally:
        conn.close()
    return inserted_history

def insert_category(category):
    inserted_category = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO categories(user_id, type, category) VALUES(?, ?, ?)",
            (category['user_id'], category['type'], category['category'])
        )
        conn.commit()
        inserted_category = get_categories_by_id_and_category(category["user_id"], category["category"])
    except:
        conn().rollback()
    finally:
        conn.close()
    return inserted_category