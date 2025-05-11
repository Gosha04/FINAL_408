import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
    host = os.getenv('MYSQL_HOST'),
    user = os.getenv('MYSQL_USERNAME'),
    password = os.getenv('MYSQL_PASSWORD'),
    auth_plugin = 'mysql_native_password'
    )
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("USE dealership")

class Address():
    def __init__(self, id, street, ZIP, cityID):
        if id is not None:
            self.id = id
        else:
            mycursor.execute("SELECT MAX(id) FROM address")
            result = mycursor.fetchone()
            max_id = result[0] if result[0] is not None else -1 # Just in case, shouldn't need that last bit
            self.id = max_id + 1

        self.street, self.ZIP, self.cityID = street, ZIP, cityID

        mycursor.execute("INSERT INTO address VALUES(%s, %s, %s, %s);", (self.id, street, ZIP, cityID))
        mydb.commit()

