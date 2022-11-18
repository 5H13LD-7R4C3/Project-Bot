import sqlite3

def addBot(id, name, ip):
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()

        sqlite_insert_with_param = """INSERT INTO bots
                          (id, bot_name, bot_ip) 
                          VALUES (?, ?, ?);"""


        data_tuple = (id, name, ip)
        cursor.execute(sqlite_insert_with_param, data_tuple)


        sqliteConnection.commit()
        print("Bot Added ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to add bot", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

a = "1"
b = "test"
c = "192.132.123.1"
addBot(a,b,c)