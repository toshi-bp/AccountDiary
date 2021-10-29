import sqlite3

#データベースを新規作成 or 読み込み
db = sqlite3.connect(
    "AccountDiary.db",              #ファイル名
    isolation_level=None,
)

#フィールド作成用SQL文

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