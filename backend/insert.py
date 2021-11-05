from create_db import connect_to_db
from get_data import get_user_by_id, get_images_by_id, get_histories_by_id, get_categories_by_id

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
    inserted_image = []
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO images(id, user_id, image_url, act_time, update_time, diary, score, cost) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
            (image['id'], image['user_id'], image['image_url'], image['act_time'], image['update_time'], image['diary'], image['score'], image['cost'])
        )
        conn.commit()
        inserted_image = get_images_by_id(image['user_id'])
    except:
        conn().rollback()
    finally:
        conn.close()
    return inserted_image[len(inserted_image)-1]

def insert_history(history):
    inserted_history = []
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO histories(id, user_id, action, result, act_time, update_time, category) VALUES(?, ?, ?, ?, ?, ?, ?)",
            (history['id'], history['user_id'], history['action'], history['result'], history['act_time'], history['update_time'], history['category'])
        )
        conn.commit()
        inserted_history = get_histories_by_id(history['user_id'])
    except:
        conn().rollback()
    finally:
        conn.close()
    return inserted_history[len(inserted_history)-1]

def insert_category(category):
    inserted_category = []
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO categories(id, user_id, type, category) VALUES(?, ?, ?, ?)",
            (category['id'], category['user_id'], category['type'], category['category'])
        )
        conn.commit()
        inserted_category = get_categories_by_id(category['user_id'])
    except:
        conn().rollback()
    finally:
        conn.close()
    return inserted_category[len(inserted_category)-1]
