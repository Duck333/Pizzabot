
import sqlite3

table_name = 'eat'

try:
    sqlite_connection = sqlite3.connect('Base.db')
    cursor = sqlite_connection.cursor()
    print("База данных sqlite создана и подключена !!!")   
except sqlite3.Error as error :
    print("Возникла ошибка",error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с sqlite закрыто")
def createTable():
    try:
        sqlite_connection = sqlite3.connect('base.db')
        cursor = sqlite_connection.cursor()
        print("База данных sqlite создана и подключена !!!")
        sqlite3_sqlite_create_query = '''CREATE TABLE IF NOT EXISTS eat(
                                              id INTEGER PRIMARY KEY,
                                              name TEXT NOT NULL);'''
        cursor.execute(sqlite3_sqlite_create_query)
        sqlite_connection.commit()
        sqlite_connection.close()
        print("Таблица eat создана")
    except sqlite3.Error as error :
     print("Возникла ошибка",error)
    finally:
     if sqlite_connection:
         sqlite_connection.close()
         print("Соединение с sqlite закрыто")
#createTable()

def readTable():
 try:   
    sqlite_connection = sqlite3.connect('Base.db')
    cursor = sqlite_connection.cursor()
    print("База данных sqlite создана и подключена !!!")

    sqlite_select_query = "SELECT * FROM eat;"
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for record in records:
        print("ID", record[0])
        print("Name", record[1])
        print()
    cursor.close()

 except sqlite3.Error as error :
    print("Возникла ошибка",error)
 finally:
     if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с sqlite закрыто")
readTable()