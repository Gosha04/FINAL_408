import mysql.connector
import os
from dotenv import load_dotenv
from workOrder import WorkOrder


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


class Employee():
    def __init__(self, id, firstName, lastName, role, dealerID, superID):
        if id is not None:
            self.id = id
        else:
            mycursor.execute("SELECT MAX(id) FROM employee")
            result = mycursor.fetchone()
            max_id = result[0] if result[0] is not None else -1 # Just in case, shouldn't need that last bit
            self.id = max_id + 1

        self.firstName = firstName
        self.lastName = lastName
        self.role = role
        self.dealerID = dealerID
        self.superID = superID

        mycursor.execute("INSERT INTO employee VALUES (%s, %s, %s, %s, %s);",
                        (id, firstName, lastName, role, dealerID, superID))
        mydb.commit()

    def updateInfo(self, item, newValue):
        mycursor.execute("UPDATE customer SET %s = %s WHERE customerID = %s;",(self.id, item, newValue))
        mydb.commit()

    def createWorkOrder(self, startDate, endDate, customerID, vehicleID, dealershipID):
        WorkOrder(startDate, endDate, customerID, self.id, vehicleID, dealershipID)


    




    