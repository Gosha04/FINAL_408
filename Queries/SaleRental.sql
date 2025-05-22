
CREATE VIEW sale_details AS
SELECT
    s.saleID,
    s.amount AS saleAmount,
    s.date AS saleDate,

    -- Customer Info
    c.customerID,
    c.firstName AS customerFirstName,
    c.lastName AS customerLastName,

    -- Employee Info
    e.employeeID,
    e.firstName AS employeeFirstName,
    e.lastName AS employeeLastName

FROM sale s
JOIN customer c ON s.customerID = c.customerID
JOIN employee e ON s.employeeID = e.employeeID;



CREATE VIEW rental_details AS
SELECT
    r.rentalID,
    r.startDate,
    r.endDate,

    -- Customer Info
    c.customerID,
    c.firstName AS customerFirstName,
    c.lastName AS customerLastName,

    -- Employee Info
    e.employeeID,
    e.firstName AS employeeFirstName,
    e.lastName AS employeeLastName

FROM rental r
JOIN customer c ON r.customerID = c.customerID
JOIN employee e ON r.employeeID = e.employeeID;


SELECT *
FROM rental_details;

SELECT *
FROM sale_details
WHERE customerID = 3;

SELECT *
FROM rental_details
WHERE customerID = 3;


-- Dealerships by city, county, state
SELECT 
    dealership.dealershipID,
    address.streetAddress,
    city.cityName,
    county.countyName,
    state.stateName
FROM dealership
INNER JOIN address ON dealership.addressID = address.addressID
INNER JOIN city ON address.cityID = city.cityID
INNER JOIN county ON city.countyID = county.countyID
INNER JOIN state ON county.stateID = state.stateID; 

-- Vehicles at each Dealership
SELECT 
    vehicle.vehicleID,
    vehicle.vin,
    vehicle.year,
    vehicle.make,
    vehicle.model,
    vehicle.color,
    vehicle.listPrice,
    vehicle.rentalRate,
    vehicle.dealershipID
FROM vehicle
INNER JOIN dealership ON vehicle.dealershipID = dealership.dealershipID
WHERE vehicle.available = 1;


-- Customer Purchase history 
SELECT 
    sale.saleID,
    sale.date,
    sale.amount,
    vehicle.make,
    vehicle.model,
    vehicle.year,
    vehicle.vin
FROM sale
INNER JOIN vehicle ON sale.vehicleID = vehicle.vehicleID
WHERE sale.customerID = ?;


-- Customer rental records 

SELECT 
    rental.rentalID,
    rental.startDate,
    rental.endDate,
    vehicle.make,
    vehicle.model,
    vehicle.year,
    vehicle.vin
FROM rental
INNER JOIN vehicle ON rental.vehicleID = vehicle.vehicleID
WHERE rental.customerID = ?;



-- Customer Open work orders 

SELECT 
    workOrder.workOrderID,
    workOrder.dateOpened,
    vehicle.make,
    vehicle.model,
    vehicle.year,
    vehicle.vin
FROM workOrder
INNER JOIN vehicle ON workOrder.vehicleID = vehicle.vehicleID
WHERE workOrder.customerID = ? AND workOrder.active = 1;








