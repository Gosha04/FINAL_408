CREATE SCHEMA dealership;

CREATE TABLE employee (
    employeeID INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(30) NOT NULL,
    lastName VARCHAR(30) NOT NULL,
    role VARCHAR(20) DEFAULT 'Trainee',
    dealershipID INT NOT NULL,
    supervisorID INT NOT NULL DEFAULT 1,
    FOREIGN KEY (dealershipID) REFERENCES dealership(dealershipID),
    FOREIGN KEY (supervisorID) REFERENCES employee(employeeID)
);

CREATE TABLE dealership(
    dealershipID INT PRIMARY KEY AUTO_INCREMENT,
    addressID INT NOT NULL UNIQUE,
    FOREIGN KEY (addressID) REFERENCES address(addressID)
);

CREATE TABLE address (
    addressID INT PRIMARY KEY AUTO_INCREMENT,
    streetAddress VARCHAR(70) NOT NULL,
    ZIP VARCHAR(5) NOT NULL,
    cityID INT NOT NULL,
    FOREIGN KEY (cityID) REFERENCES city(cityID)
);

CREATE TABLE county (
    countyID INT PRIMARY KEY AUTO_INCREMENT,
    countyName VARCHAR(30) NOT NULL,
    stateID INT NOT NULL,
    FOREIGN KEY (stateID) REFERENCES state(stateID)
);


CREATE TABLE state (
    stateID INT PRIMARY KEY AUTO_INCREMENT,
    stateName VARCHAR(25) NOT NULL,
    abbreviation CHAR(2) NOT NULL
);

CREATE TABLE customer (
    customerID INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(30) NOT NULL,
    lastName VARCHAR(30) NOT NULL,
    addressID INT,
    FOREIGN KEY (addressID) REFERENCES address(addressID)
);

CREATE TABLE vehicle (
    vehicleID INT PRIMARY KEY AUTO_INCREMENT,
    vin CHAR(17) NOT NULL UNIQUE,
    year CHAR(4),
    make VARCHAR(20),
    model VARCHAR(20),
    color VARCHAR(30),
    available BOOLEAN NOT NULL DEFAULT TRUE,
    used BOOLEAN NOT NULL DEFAULT FALSE,
    dealershipID INT NOT NULL,
    listPrice INT NOT NULL,
    rentalRate INT NOT NULL,
    FOREIGN KEY (dealershipID) REFERENCES dealership(dealershipID)
);

CREATE TABLE sale (
    saleID INT PRIMARY KEY AUTO_INCREMENT,
    amount INT NOT NULL,
    date DATE NOT NULL,
    employeeID INT NOT NULL,
    customerID INT NOT NULL,
    dealershipID INT NOT NULL,
    FOREIGN KEY (employeeID) REFERENCES employee(employeeID),
    FOREIGN KEY (customerID) REFERENCES customer(customerID),
    FOREIGN KEY (dealershipID) REFERENCES dealership(dealershipID)
);

CREATE TABLE rental (
    rentalID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    startDate DATE NOT NULL,
    endDate DATE,
    vehicleID INT NOT NULL,
    employeeID INT NOT NULL,
    customerID INT NOT NULL,
    dealershipID INT NOT NULL,
    FOREIGN KEY (employeeID) REFERENCES employee(employeeID),
    FOREIGN KEY (customerID) REFERENCES customer(customerID),
    FOREIGN KEY (dealershipID) REFERENCES dealership(dealershipID),
    FOREIGN KEY (vehicleID) REFERENCES vehicle(vehicleID)
);

CREATE TABLE workOrder (
    workOrderID INT PRIMARY KEY AUTO_INCREMENT,
    dateOpened DATE NOT NULL,
    active BOOLEAN NOT NULL DEFAULT TRUE,
    customerID INT NOT NULL,
    vehicleID INT NOT NULL,
    dealershipID INT NOT NULL,
    FOREIGN KEY (customerID) REFERENCES customer(customerID),
    FOREIGN KEY (vehicleID) REFERENCES vehicle(vehicleID),
    FOREIGN KEY (dealershipID) REFERENCES dealership(dealershipID)
);

CREATE TABLE employeeWorkOrder (
    employeeID INT NOT NULL,
    workOrderID INT NOT NULL,
    PRIMARY KEY (employeeID, workOrderID),
    FOREIGN KEY (employeeID) REFERENCES employee(employeeID),
    FOREIGN KEY (workOrderID) REFERENCES workOrder(workOrderID)
);

CREATE TABLE city (
    cityID INT PRIMARY KEY AUTO_INCREMENT,
    cityName VARCHAR(20) NOT NULL,
    countyID INT NOT NULL,
    FOREIGN KEY (countyID) REFERENCES county(countyID)
);

ALTER TABLE workOrder
ADD COLUMN dealershipID INT NOT NULL;

ALTER TABLE workOrder
ADD FOREIGN KEY (dealershipID) REFERENCES dealership(dealershipID);

ALTER TABLE sale
ADD COLUMN vehicleID INT NOT NULL;

ALTER TABLE sale
ADD FOREIGN KEY (vehicleID) REFERENCES vehicle(vehicleID);



