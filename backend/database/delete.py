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

def delete_images(user_id):
    message = {}

def delete_histories(user_id):
    message = {}