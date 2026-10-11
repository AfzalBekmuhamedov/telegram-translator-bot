from psycopg2 import connect
from config import DATABASE_NAME,DATABASE_USER,DATABASE_PASSWORD,DATABASE_HOST,DATABASE_PORT

class DataBase:
    def __init__(self):
        self.connect = connect(
            database=DATABASE_NAME,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            host=DATABASE_HOST,
            port=DATABASE_PORT
        )
    def manager(self,sql,*args,fetchall=False,commit=False):
        with self.connect as db:
            cursor = db.cursor()
            cursor.execute(sql,args)
            if fetchall:
                return cursor.fetchall()
            elif commit:
                return db.commit()

    def crate_table(self):
        sql = """CREATE TABLE IF NOT EXISTS words(
        id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        chat_id BIGINT,
        word VARCHAR(500),
        translated_word VARCHAR(500) 
        )"""
        self.manager(sql,commit=True)

    def insert_table(self,chat_id,word,translated_word):
        sql = "INSERT INTO words(chat_id,word,translated_word) VALUES (%s,%s,%s)"
        self.manager(sql,chat_id,word,translated_word,commit=True)

    def select_table(self,chat_id):
        sql = "SELECT word, translated_word FROM words WHERE chat_id = %s ORDER BY id DESC LIMIT 6"
        return self.manager(sql,chat_id,fetchall=True)


