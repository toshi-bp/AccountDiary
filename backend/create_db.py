import sqlite3

# データベースと接続するための関数
def connect_to_db():
    #データベースを新規作成 or 読み込み
    db = sqlite3.connect(
        # データベースのファイル名(pathに注意)
        "AccountDiary.db",
        isolation_level=None,
    )
    return db

def create_tables():
    #フィールド作成用SQL文
    try:
        conn = connect_to_db()
        # ユーザー情報テーブル
        conn.execute('''
            CREATE TABLE users (
                id TEXT primary key not null,
                mail TEXT not null,
                password TEXT not null,
                name TEXT not null,
                birthday TEXT not null,
                gender TEXT not null,
                phonenumber TEXT not null,
                money INTEGER not null,
                used_money INTEGER not null,
                jti TEXT default null
            );
        ''')
        # 画像情報テーブル
        conn.execute('''
            CREATE TABLE images (
                id Integer primary key autoincrement,
                user_id TEXT,
                image_url TEXT not null,
                act_time DataTime not null,
                update_time DateTime not null,
                diary TEXT not null,
                score Integer,
                foreign key (user_id) references users(id)
            );
        ''')
        # 行動履歴テーブル
        conn.execute('''
            CREATE TABLE histories (
                id Integer primary key autoincrement,
                user_id TEXT,
                action TEXT not null,
                result Integer not null, 
                act_time Date not null, 
                update_time Date not null,
                category TEXT not null,
                place TEXT not null,
                foreign key (user_id) references users(id)
            );
        ''')
        # カテゴリー
        conn.execute('''
            CREATE TABLE categories (
                id Integer primary key autoincrement,
                user_id TEXT,
                type TEXT not null,
                category TEXT not null,
                foreign key (user_id) references users(id)
            );
        ''')
        conn.commit()
        print('Tables created success!!')
    except:
        print('Tables creation failed...')
    finally:
        conn.close()

if __name__ == '__main__':
    create_tables()