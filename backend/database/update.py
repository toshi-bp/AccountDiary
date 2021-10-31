from create_db import connect_to_db
from get_data import get_user_by_id, get_images_by_id, get_histories_by_id

def update_user(user):
    updated_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("""
            UPDATE users SET name = ?
        """)
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

def update_history(history):
    updated_history = {}