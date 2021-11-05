from create_db import connect_to_db
from get_data import get_user_by_id, get_images_by_id, get_histories_by_id

# usersのあるカラムを更新するための関数
def update_user(user):
    updated_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE users SET jti = ? WHERE id = ?", (user["jti"], user["id"]))
        conn.commit()
        updated_user = get_user_by_id(user["id"])
    except:
        conn.rollback()
        updated_user = {}
    finally:
        conn.close()
    return updated_user

# jtiを更新する関数
def update_user_jti(user, access_token):
    updated_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE users SET jti = ? WHERE id = ?", (access_token, user["id"]))
        conn.commit()
        updated_user = get_user_by_id(user["id"])
    except:
        conn.rollback()
        updated_user = {}
    finally:
        conn.close()
    return updated_user

# imagesとhistoryは更新をできないようにしても良いのでは？？
def update_image(image):
    updated_image = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("""
            UPDATE images SET
        """)
        conn.commit()
        updated_image = get_images_by_id(image["user_id"])
    except:
        conn.rollback()
    finally:
        conn.close()
    return updated_image




# パスワードの変更
def update_user_pwd(user, password):
    updated_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE users SET password = ? WHERE id = ?", (password, user["id"]))
        conn.commit()
        updated_user = get_user_by_id(user["id"])
    except:
        conn.rollback()
        updated_user = {}
    finally:
        conn.close()
    return updated_user

# 予算の変更
def update_user_money(user, money):
    updated_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE users SET money = ? WHERE id = ?", (money, user["id"]))
        conn.commit()
        updated_user = get_user_by_id(user["id"])
    except:
        conn.rollback()
        updated_user = {}
    finally:
        conn.close()
    return updated_user

# カテゴリの変更
def update_hisotries_category(category, change_category):
    updated_category = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE histories SET category = ? WHERE id = ?", (change_category, user["id"]))
        conn.commit()
        updated_category = updated_categories_by_id(category["id"])
    except:
        conn.rollback()
        updated_category = {}
    finally:
        conn.close()
    return updated_category