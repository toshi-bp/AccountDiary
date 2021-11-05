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

def delete_histories(id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from histories WHERE id = ?", (id,))
        conn.commit()
        message["status"] = "success"
    except:
        conn.rollback()
        message["status"] = "failed"
    finally:
        conn.close()
    return message

def delete_categories(id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from categories WHERE id = ?", (id,))
        conn.commit()
        message["status"] = "success"
    except:
        conn.rollback()
        message["status"] = "failed"
    finally:
        conn.close()
    return message