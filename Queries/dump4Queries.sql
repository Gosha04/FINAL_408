
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