import mysql.connector
from Init import *
class MySQLConnector:
    def __init__(self):
        self.host = DB_HOST
        self.user = DB_USER
        self.password = DB_PASSWORD
        self.database = DB_DATABASE
        self.conn = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
           # if self.conn.is_connected():
           #    print("Conexión exitosa a la base de datos MySQL")
        except mysql.connector.Error as err:
            print("Error connecting database MySQL:", err)

    def execute_query(self, query):
        if not self.conn:
            return None

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except mysql.connector.Error as err:
            return None

    def close(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
