INSERT INTO state(stateName, abbreviation)
VALUES ('California', 'CA'),
       ('Oregon', 'OR'),
       ('Washington', 'WI'),
       ('Texas', 'TX'),
       ('Wisconsin', 'WI');

INSERT INTO county(countyName, stateID)
VALUES ('Contra Costa', 1),
       ('Orange', 1),
       ('Placer', 1),
       ('Deschutes', 2),
       ('Umatilla', 2),
       ('Clatsop', 2),
       ('Chelan', 3),
       ('Grays Harbor',3),
       ('Pend Oreille', 3),
       ('Llano', 4),
       ('Jeff Davis', 4),
       ('Fannin', 4),
       ('Pepin', 5),
       ('Dodge', 5),
       ('Kewaunee', 5);

INSERT INTO city(cityName, countyID)
VALUES ('Pittsburg', 1),
       ('Brentwood', 1),
       ('Orinda', 1),
       ('Tustin', 2),
       ('Laguna Niguel', 2),
       ('Fullerton', 2),
       ('Rocklin', 3),
       ('Colfax', 3),
       ('Sisters', 4),
       ('La Pine', 4),
       ('Echo', 5),
       ('Helix', 5),
       ('Gearhart', 6),
       ('Warrenton', 6),
       ('Entiat', 7),
       ('Leavenworth', 7),
       ('Cosmopolis', 8),
       ('Elma', 8),
       ('Ione', 9),
       ('Metaline Falls', 9),
       ('Llano', 10),
       ('Sunrise Beach Village', 10),
       ('Valentine', 11),
       ('Fort Davis', 11),
       ('Bonham', 12),
       ('Leonard', 12),
       ('Durand', 13),
       ('Pepin', 13),
       ('Mayville', 14),
       ('Fox Lake', 14),
       ('Kewaunee', 15),
       ('Algoma', 15);

INSERT INTO address(streetAddress, ZIP, cityID)
VALUES ('1234 Harbor Street', '94565', 1),
       ('5678 Acacia Avenue', '92831', 6),
       ('910 3rd Street', '54216', 31),
       ('4321 Main Street', '95713', 8),
       ('2437 Park Avenue', '92782', 4);

INSERT INTO customer (firstName, lastName)
VALUES ('John', 'Doe'),
       ('Jane', 'Doe');

INSERT INTO customer (firstName, lastName, addressID)
VALUES ('Frank', 'Gribbelwolder', 1),
       ('Harold', 'Wren', 2);

INSERT INTO dealership(addressID)
VALUES (3),
       (4),
       (5);

INSERT INTO employee(firstName, lastName, role, dealershipID, supervisorID)
VALUES ('Charlie','Funk', 'Owner', 1, 1),
       ('Marissa','Kletterman', 'Manager', 1, 1),
       ('Maximilian','Kirkorian', 'Manager', 2, 1),
       ('Joshua','Reynolds', 'Manager', 3, 1),
       ('Ryland','Frimpong', 'Salesperson', 1, 2),
       ('Florian','Kane', 'Salesperson', 2, 3),
       ('Bert','Bertovich', 'Salesperson', 3, 4),
       ('Luke','Arthem', 'Technician', 1, 2),
       ('Arno','Hunter', 'Technician', 2, 3),
       ('Albert','Mueller', 'Technician', 3, 4);

INSERT INTO employee(firstName, lastName, dealershipID, supervisorID)
VALUES ('Kim', 'Jenkins', 1, 5),
       ('Kirk', 'Attaman', 2, 6),
       ('Bobert', 'Boblopian', 1, 8);

INSERT INTO vehicle(vin, year, make, model, color, dealershipID, listPrice, rentalRate)
VALUES ('1HGCM82633A004352', 2016, 'Toyota', '4Runner', 'Gray', 1, 30000, 30);

INSERT INTO vehicle(vin, dealershipID, listPrice, rentalRate)
VALUES ('3FAHP0HA8AR123456', 2, 19000, 19),
       ('JHMBA7450GC012345', 3, 40000, 40);

INSERT INTO vehicle(vin, available, dealershipID, listPrice, rentalRate)
VALUES ('1FTFW1ET4EFA12345', 0, 1, 20000, 20),
       ('2C3CDXBG8KH512678', 0, 1, 20000, 20),
       ('WDBUF56X58B321987', 0, 1, 20000, 20);

INSERT INTO sale (amount, date, employeeID, customerID, dealershipID, vehicleID)
VALUES (20000, '2025-1-2', 1, 1, 1, 4),
       (20000, '2025-1-2', 1, 2, 1, 5),
       (20000, '2025-1-2', 1, 3, 1, 6);

INSERT INTO vehicle(vin, available, dealershipID, listPrice, rentalRate)
VALUES ('1GNEK13ZX3R765432', 0, 1, 20000, 20),
       ('JN1AZ34D34T123789', 0, 1, 20000, 20),
       ('KM8J33A28JU556001', 0, 1, 20000, 20);

INSERT INTO rental(startDate, vehicleID, employeeID, customerID, dealershipID)
VALUES ('2025-2-2', 7, 1, 1, 1),
       ('2025-2-2', 8, 1, 2, 1),
       ('2025-2-2', 9, 1, 4, 1);

INSERT INTO workOrder (dateOpened, customerID, vehicleID, dealershipID)
VALUES ('2025-3-3', 1, 4, 1),
       ('2025-3-3', 2, 5, 1),
       ('2025-3-3', 3, 6, 1);

INSERT INTO employeeWorkOrder
VALUES (8, 1),
       (8, 2),
       (8,3);

UPDATE sale
SET employeeID = 5;

UPDATE rental
SET employeeID = 5;