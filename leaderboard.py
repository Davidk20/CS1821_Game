import sqlite3
from sqlite3 import Error

class Leaderboard:
    def __init__(self):
        self.create_connection()
        if self.con is not None:
            self.create_table()


    def create_connection(self):
        try:
            self.con = sqlite3.connect("leaderboard.db")
            self.cur = self.con.cursor()

        except Error as err:
            print(err)
        

    def create_table(self):
        try:
            self.cur.execute('''
            CREATE TABLE IF NOT EXISTS leaderboard(
                id integer PRIMARY KEY AUTOINCREMENT,
                name text NOT NULL,
                score integer NOT NULL
            );
            ''')
        except Error as err:
            print(err)
        

    def close(self):
        self.con.close()
        