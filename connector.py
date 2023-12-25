import mysql.connector
from prettytable import from_db_cursor

class database:
    def connect(self):
        self.db = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='Bimbel_pbop'
        )
        self.cur = self.db.cursor()

    def create(self, query):
        try:
            self.cur.execute(query)
            self.db.commit()
        except Exception as e:
            print(f"Error creating table: {e}")

    def insertValue(self, query, data):
        try:
            self.cur.execute(query, data)
            self.db.commit()
        except Exception as e:
            print(f"Error inserting data: {e}")

    def selectValue(self, query, data=None):
        try:
            self.cur.execute(query, data)
            result = self.cur.fetchall()
            return result
        except Exception as e:
            print(f"Error executing query: {e}")
            return None
        
    def selectValuepretty(self, query, data) :
        try:
            self.cur.execute(query, data)
            mytable = from_db_cursor(self.cur)
            return print(mytable)
        except Exception as e:
            print(f"Error executing query: {e}")
            return None