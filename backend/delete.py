from create_db import connect_to_db

def delete_user(user_id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from users WHERE id = ?", (user_id,))
        conn.commit()
        message["status"] = "User deleted successfully!"
    except:
        conn.rollback()
        message["status"] = "Cannot delete user"
    finally:
        conn.close()
    return message

def delete_images(id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from images WHERE id = ?", (id,))
        conn.commit()
        message["status"] = "success"
    except:
        conn.rollback()
        message["status"] = "failed"
    finally:
        conn.close()
    return message

def delete_histories(user_id,action):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from histories WHERE user_id = ? and action = ?", (user_id,action))
        conn.commit()
        message["status"] = "success"
    except:
        conn.rollback()
        message["status"] = "failed"
    finally:
        conn.close()
    return message

def delete_categories(user_id,category):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from categories WHERE user_id = ? and category = ?", (user_id,category))
        conn.commit()
        message["status"] = "success"
    except:
        conn.rollback()
        message["status"] = "failed"
    finally:
        conn.close()
    return message