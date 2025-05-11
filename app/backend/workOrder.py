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

class WorkOrder():
    def __init__ (self, startDate, endDate, customerID, employeeID, vehicleID, dealershipID):
        mycursor.execute("SELECT MAX(id) FROM workOrder")
        result = mycursor.fetchone()
        max_id = result[0] if result[0] is not None else -1 # Just in case, shouldn't need that last bit

        self.id = max_id + 1
        self.startDate = startDate
        self.endDate = endDate
        self.customerID = customerID
        self.employeeID = employeeID
        self.vehicleID = vehicleID
        self.dealershipID = dealershipID

        mycursor.execute("INSERT INTO workOrder VALUES (%s, %s, %s, %s, %s, %s, %s);", 
                        (self.id, startDate, endDate, customerID, employeeID, vehicleID, dealershipID))
        
        mycursor.execute("INSERT INTO employeeWorkOrder VALUES (%s, %s);",(self.id, employeeID))
        mydb.commit()

    