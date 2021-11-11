from create_db import connect_to_db
from get_data import get_user_by_id, get_images_by_id, get_histories_by_id, get_categories_by_id

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
def update_user_pwd(user_id, password):
    updated_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE users SET password = ? WHERE id = ?", (password, user_id))
        conn.commit()
        updated_user = get_user_by_id(user_id)
    except:
        conn.rollback()
        updated_user = {}
    finally:
        conn.close()
    return updated_user

# 予算の変更
def update_user_money(user_id, change_money, type):
    updated_user = {}
    print("type:")
    print(type)
    user_data = get_user_by_id(user_id)
    user_money = user_data["money"]
    user_used_money = user_data["used_money"]
    """
    if income
        money += change_money
    else
        used_money += change_money
    get_data関数を用いてデータを取得し, 計算した値を格納することとする
    """
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        if (type == 'income'):
            result = user_money + change_money
            print('result:')
            print(result)
            cur.execute("UPDATE users SET money = ? WHERE id = ?", (result, user_id))
            conn.commit()
            updated_user = get_user_by_id(user_id)
        elif (type == 'expenditure'):
            used_result = user_used_money + change_money
            print('used_result:')
            print(used_result)
            cur.execute("UPDATE users SET used_money = ? WHERE id = ?", (used_result, user_id))
            conn.commit()
            updated_user = get_user_by_id(user_id)
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
        cur.execute("UPDATE histories SET category = ? WHERE user_id = ? and category = ?", (change_category, category["user_id"], category["category"]))
        conn.commit()
        updated_category = get_categories_by_id(category["user_id"])
    except:
        conn.rollback()
        updated_category = {}
    finally:
        conn.close()
    return updated_category