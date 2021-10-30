import sqlite3

# データベースと接続するための関数
def connect_to_db():
    #データベースを新規作成 or 読み込み
    db = sqlite3.connect(
        # データベースのファイル名(pathに注意)
        "AccountDiary.db",
        isolation_level=None,
    )

def create_tables():
    #フィールド作成用SQL文
    try:
        conn = connect_to_db()
        # ユーザー情報テーブル
        conn.execute('''
            CREATE TABLE user (
                id Integer primary key,
                mail TEXT not null,
                pwd TEXT not null,
                name TEXT not null,
                birthday TEXT not null,
                gender TEXT not null,
                phonenumber TEXT not null
            );
        ''')
        # 画像情報テーブル
        conn.execute('''
            CREATE TABLE images (
                id Integer primary key not null,
                user_id Integer,
                image_url TEXT not null,
                act_time DataTime not null,
                update_time DateTime not null,
                diary TEXT not null,
                score Integer,
                foreign key (memberid) references membership(id)
            );
        ''')
        # 行動履歴テーブル
        conn.execute('''
            CREATE TABLE history (
                id Integer primary key, 
                memberid Integer,
                action TEXT not null,
                result Integer not null, 
                act_time Date not null, 
                update_time Date not null,
                category TEXT not null,
                foreign key (memberid) references membership(id)
            );
        ''')
        conn.commit()
        print('Tables created success!!')
    except:
        print('Tables creation failed...')
    finally:
        conn.close()

# ユーザー情報を挿入するための関数
def insert_user(user):
    inserted_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            ""
        )
        conn.commit()
        inserted_user = get_user_by_id(cur.lastrowid)
    except:
        conn().rollback()
    finally:
        conn.close()
    return inserted_user


sql_membership = """
    CREATE TABLE membership (
        id Integer primary key, 
        mail TEXT not null, 
        pwd TEXT not null,
        birthday TEXT not null, 
        gender TEXT not null, 
        phonenumber Integer not null
    );
"""


sql_images = """
    CREATE TABLE images (
        id Integer primary key not null, 
        memberid Integer, 
        image_url TEXT not null,
        act_time DataTime not null, 
        update_time DateTime not null, 
        diary TEXT not null,
        foreign key (memberid) references membership(id)
    );
"""




sql_history = """
    CREATE TABLE history (
        id Integer primary key, 
        memberid Integer,
        action TEXT not null,
        result Integer not null, 
        act_time Date not null, 
        update_time Date not null,
        category TEXT not null,
        foreign key (memberid) references membership(id)
    );
"""




sql2 = """
    INSERT INTO membership VALUES (
        1, 2, 3, 4, 5, 6
    )
"""


sql3 = """
    SELECT * FROM membership   
"""

# db.execute(sql_membership)
# db.execute(sql_images)
# db.execute(sql_history)

db.execute(sql2)

for i in db.execute(sql3):
    print(i)

db.close()         