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

        mycursor.execute("INSERT INTO customer VALUES (%s, %s, %s);", (firstName, lastName, addressID))
        mydb.commit()
    

    def findDealership(placeType, placeName): # placeType and placeName should be stripped
        mycursor.execute("""SELECT dealership.Name FROM dealerShip
                        INNER JOIN %s ON %sID = %s %sID
                        WHERE dealership.%sName = %s;""", (placeType, placeType, placeType, placeType, placeType, placeName))
        
    def findCarsAvailable(dealerID):
        mycursor.execute("SELECT * FROM vehicle WHERE dealershipID = %s;", (dealerID,))

    def purchaseRecord(self):
        mycursor.execute("""SELECT * FROM vehicle INNER JOIN sales ON customer.customerID = sales.customerID 
                    INNER JOIN vehicle ON sales.vehicleID = vehicle.vehicleID WHERE customer.customerID = %s;""", (self.id,))

    def rentalRecord(self):
        mycursor.execute("""SELECT * FROM vehicle INNER JOIN rental ON customer.customerID = rental.customerID 
                    INNER JOIN vehicle ON rental.vehicleID = vehicle.vehicleID WHERE customer.customerID = %s;""", (self.id,))
        
    def workOrderRecord(self):
            mycursor.execute("SELECT * FROM workOrder WHERE customerID = %s;", (self.id,))

    def viewAddressInfo(self):
        mycursor.execute("""CREATE VIEW IF NOT EXISTS addressInfo AS
                        SELECT address.streetAddress, city.cityName, county.countyName, state.stateName
                        FROM address, city, county, state;""")
        mydb.commit()
        
        mycursor.execute("SELECT * FROM addressInfo;")

    



    