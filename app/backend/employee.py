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


class employee():
    def __init__(self, id, firstName, lastName, role, dealerID, superID):
        self.firstName = firstName
        self.lastName = lastName
        self.role = role
        self.dealerID = dealerID
        self.superID = superID
        self.id = id

        mycursor.execute("INSERT INTO employee VALUES (%s, %s, %s, %s, %s);",
                        (id, firstName, lastName, role, dealerID, superID))
        mydb.commit()

    