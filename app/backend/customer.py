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

class Customer:
    def __init__(self, id, firstName, lastName, addressID):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.addressID = addressID

    def findDealership(placeType, placeName): # placeType and placeName should be stripped
        mycursor.execute("""SELECT Name FROM dealerShip
                        INNER JOIN %s ON dealership %sID = %s %sID
                        WHERE %sName = %s;""", (placeType, placeType, placeType, placeType, placeName))
        
    # def findCarsAvailable():


    