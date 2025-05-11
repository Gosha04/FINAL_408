-- MySQL dump 10.13  Distrib 9.2.0, for macos14.7 (arm64)
--
-- Host: 127.0.0.1    Database: dealership
-- ------------------------------------------------------
-- Server version	9.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `address`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
USE dealership_db;
CREATE TABLE `address` (
  `addressID` int NOT NULL AUTO_INCREMENT,
  `streetAddress` varchar(70) NOT NULL,
  `ZIP` varchar(5) NOT NULL,
  `cityID` int NOT NULL,
  PRIMARY KEY (`addressID`),
  KEY `cityID` (`cityID`),
  CONSTRAINT `address_ibfk_1` FOREIGN KEY (`cityID`) REFERENCES `city` (`cityID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

INSERT INTO `address` VALUES (1,'1234 Harbor Street','94565',1),(2,'5678 Acacia Avenue','92831',6),(3,'910 3rd Street','54216',31),(4,'4321 Main Street','95713',8),(5,'2437 Park Avenue','92782',4);

--
-- Table structure for table `city`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `city` (
  `cityID` int NOT NULL AUTO_INCREMENT,
  `cityName` varchar(100) NOT NULL,
  `countyID` int NOT NULL,
  PRIMARY KEY (`cityID`),
  KEY `countyID` (`countyID`),
  CONSTRAINT `city_ibfk_1` FOREIGN KEY (`countyID`) REFERENCES `county` (`countyID`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `city`
--

INSERT INTO `city` VALUES (1,'Pittsburg',1),(2,'Brentwood',1),(3,'Orinda',1),(4,'Tustin',2),(5,'Laguna Niguel',2),(6,'Fullerton',2),(7,'Rocklin',3),(8,'Colfax',3),(9,'Sisters',4),(10,'La Pine',4),(11,'Echo',5),(12,'Helix',5),(13,'Gearhart',6),(14,'Warrenton',6),(15,'Entiat',7),(16,'Leavenworth',7),(17,'Cosmopolis',8),(18,'Elma',8),(19,'Ione',9),(20,'Metaline Falls',9),(21,'Llano',10),(22,'Sunrise Beach Village',10),(23,'Valentine',11),(24,'Fort Davis',11),(25,'Bonham',12),(26,'Leonard',12),(27,'Durand',13),(28,'Pepin',13),(29,'Mayville',14),(30,'Fox Lake',14),(31,'Kewaunee',15),(32,'Algoma',15);

--
-- Table structure for table `county`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `county` (
  `countyID` int NOT NULL AUTO_INCREMENT,
  `countyName` varchar(30) NOT NULL,
  `stateID` int NOT NULL,
  PRIMARY KEY (`countyID`),
  KEY `stateID` (`stateID`),
  CONSTRAINT `county_ibfk_1` FOREIGN KEY (`stateID`) REFERENCES `state` (`stateID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `county`
--

INSERT INTO `county` VALUES (1,'Contra Costa',1),(2,'Orange',1),(3,'Placer',1),(4,'Deschutes',2),(5,'Umatilla',2),(6,'Clatsop',2),(7,'Chelan',3),(8,'Grays Harbor',3),(9,'Pend Oreille',3),(10,'Llano',4),(11,'Jeff Davis',4),(12,'Fannin',4),(13,'Pepin',5),(14,'Dodge',5),(15,'Kewaunee',5);

--
-- Table structure for table `customer`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customerID` int NOT NULL AUTO_INCREMENT,
  `firstName` varchar(30) NOT NULL,
  `lastName` varchar(30) NOT NULL,
  `addressID` int DEFAULT NULL,
  PRIMARY KEY (`customerID`),
  KEY `addressID` (`addressID`),
  CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`addressID`) REFERENCES `address` (`addressID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` VALUES (1,'John','Doe',NULL),(2,'Jane','Doe',NULL),(3,'Frank','Gribbelwolder',1),(4,'Harold','Wren',2);

--
-- Table structure for table `dealership`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dealership` (
  `dealershipID` int NOT NULL AUTO_INCREMENT,
  `addressID` int NOT NULL,
  PRIMARY KEY (`dealershipID`),
  UNIQUE KEY `addressID` (`addressID`),
  CONSTRAINT `dealership_ibfk_1` FOREIGN KEY (`addressID`) REFERENCES `address` (`addressID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dealership`
--

INSERT INTO `dealership` VALUES (1,3),(2,4),(3,5);

--
-- Table structure for table `employee`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `employeeID` int NOT NULL AUTO_INCREMENT,
  `firstName` varchar(30) NOT NULL,
  `lastName` varchar(30) NOT NULL,
  `role` varchar(20) DEFAULT 'Trainee',
  `dealershipID` int NOT NULL,
  `supervisorID` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`employeeID`),
  KEY `dealershipID` (`dealershipID`),
  KEY `supervisorID` (`supervisorID`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`dealershipID`) REFERENCES `dealership` (`dealershipID`),
  CONSTRAINT `employee_ibfk_2` FOREIGN KEY (`supervisorID`) REFERENCES `employee` (`employeeID`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` VALUES (1,'Charlie','Funk','Owner',1,1),(2,'Marissa','Kletterman','Manager',1,1),(3,'Maximilian','Kirkorian','Manager',2,1),(4,'Joshua','Reynolds','Manager',3,1),(5,'Ryland','Frimpong','Salesperson',1,2),(6,'Florian','Kane','Salesperson',2,3),(7,'Bert','Bertovich','Salesperson',3,4),(8,'Luke','Arthem','Technician',1,2),(9,'Arno','Hunter','Technician',2,3),(10,'Albert','Mueller','Technician',3,4),(11,'Kim','Jenkins','Trainee',1,5),(12,'Kirk','Attaman','Trainee',2,6),(13,'Bobert','Boblopian','Trainee',1,8);

--
-- Table structure for table `employeeWorkOrder`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employeeWorkOrder` (
  `employeeID` int NOT NULL,
  `workOrderID` int NOT NULL,
  PRIMARY KEY (`employeeID`,`workOrderID`),
  KEY `workOrderID` (`workOrderID`),
  CONSTRAINT `employeeworkorder_ibfk_1` FOREIGN KEY (`employeeID`) REFERENCES `employee` (`employeeID`),
  CONSTRAINT `employeeworkorder_ibfk_2` FOREIGN KEY (`workOrderID`) REFERENCES `workOrder` (`workOrderID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employeeWorkOrder`
--

INSERT INTO `employeeWorkOrder` VALUES (8,1),(8,2),(8,3);

--
-- Table structure for table `rental`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rental` (
  `rentalID` int NOT NULL AUTO_INCREMENT,
  `startDate` date NOT NULL,
  `endDate` date DEFAULT NULL,
  `vehicleID` int NOT NULL,
  `employeeID` int NOT NULL,
  `customerID` int NOT NULL,
  `dealershipID` int NOT NULL,
  PRIMARY KEY (`rentalID`),
  KEY `employeeID` (`employeeID`),
  KEY `customerID` (`customerID`),
  KEY `dealershipID` (`dealershipID`),
  KEY `vehicleID` (`vehicleID`),
  CONSTRAINT `rental_ibfk_1` FOREIGN KEY (`employeeID`) REFERENCES `employee` (`employeeID`),
  CONSTRAINT `rental_ibfk_2` FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`),
  CONSTRAINT `rental_ibfk_3` FOREIGN KEY (`dealershipID`) REFERENCES `dealership` (`dealershipID`),
  CONSTRAINT `rental_ibfk_4` FOREIGN KEY (`vehicleID`) REFERENCES `vehicle` (`vehicleID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rental`
--

INSERT INTO `rental` VALUES (1,'2025-02-02',NULL,7,5,1,1),(2,'2025-02-02',NULL,8,5,2,1),(3,'2025-02-02',NULL,9,5,4,1);

--
-- Table structure for table `sale`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sale` (
  `saleID` int NOT NULL AUTO_INCREMENT,
  `amount` int NOT NULL,
  `date` date NOT NULL,
  `employeeID` int NOT NULL,
  `customerID` int NOT NULL,
  `dealershipID` int NOT NULL,
  `vehicleID` int NOT NULL,
  PRIMARY KEY (`saleID`),
  KEY `employeeID` (`employeeID`),
  KEY `customerID` (`customerID`),
  KEY `dealershipID` (`dealershipID`),
  KEY `vehicleID` (`vehicleID`),
  CONSTRAINT `sale_ibfk_1` FOREIGN KEY (`employeeID`) REFERENCES `employee` (`employeeID`),
  CONSTRAINT `sale_ibfk_2` FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`),
  CONSTRAINT `sale_ibfk_3` FOREIGN KEY (`dealershipID`) REFERENCES `dealership` (`dealershipID`),
  CONSTRAINT `sale_ibfk_4` FOREIGN KEY (`vehicleID`) REFERENCES `vehicle` (`vehicleID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sale`
--

INSERT INTO `sale` VALUES (1,20000,'2025-01-02',5,1,1,4),(2,20000,'2025-01-02',5,2,1,5),(3,20000,'2025-01-02',5,3,1,6);

--
-- Table structure for table `state`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `state` (
  `stateID` int NOT NULL AUTO_INCREMENT,
  `stateName` varchar(25) NOT NULL,
  `abbreviation` char(2) NOT NULL,
  PRIMARY KEY (`stateID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `state`
--

INSERT INTO `state` VALUES (1,'California','CA'),(2,'Oregon','OR'),(3,'Washington','WA'),(4,'Texas','TX'),(5,'Wisconsin','WI');

--
-- Table structure for table `vehicle`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicle` (
  `vehicleID` int NOT NULL AUTO_INCREMENT,
  `vin` char(17) NOT NULL,
  `year` char(4) DEFAULT NULL,
  `make` varchar(20) DEFAULT NULL,
  `model` varchar(20) DEFAULT NULL,
  `color` varchar(30) DEFAULT NULL,
  `available` tinyint(1) NOT NULL DEFAULT '1',
  `used` tinyint(1) NOT NULL DEFAULT '0',
  `dealershipID` int NOT NULL,
  `listPrice` int NOT NULL,
  `rentalRate` int NOT NULL,
  PRIMARY KEY (`vehicleID`),
  UNIQUE KEY `vin` (`vin`),
  KEY `dealershipID` (`dealershipID`),
  CONSTRAINT `vehicle_ibfk_1` FOREIGN KEY (`dealershipID`) REFERENCES `dealership` (`dealershipID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicle`
--

INSERT INTO `vehicle` VALUES (1,'1HGCM82633A004352','2016','Toyota','4Runner','Gray',1,0,1,30000,30),(2,'3FAHP0HA8AR123456',NULL,NULL,NULL,NULL,1,0,2,19000,19),(3,'JHMBA7450GC012345',NULL,NULL,NULL,NULL,1,0,3,40000,40),(4,'1FTFW1ET4EFA12345',NULL,NULL,NULL,NULL,0,0,1,20000,20),(5,'2C3CDXBG8KH512678',NULL,NULL,NULL,NULL,0,0,1,20000,20),(6,'WDBUF56X58B321987',NULL,NULL,NULL,NULL,0,0,1,20000,20),(7,'1GNEK13ZX3R765432',NULL,NULL,NULL,NULL,0,0,1,20000,20),(8,'JN1AZ34D34T123789',NULL,NULL,NULL,NULL,0,0,1,20000,20),(9,'KM8J33A28JU556001',NULL,NULL,NULL,NULL,0,0,1,20000,20);

--
-- Table structure for table `workOrder`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `workOrder` (
  `workOrderID` int NOT NULL AUTO_INCREMENT,
  `dateOpened` date NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '1',
  `customerID` int NOT NULL,
  `vehicleID` int NOT NULL,
  `dealershipID` int NOT NULL,
  PRIMARY KEY (`workOrderID`),
  KEY `customerID` (`customerID`),
  KEY `vehicleID` (`vehicleID`),
  KEY `dealershipID` (`dealershipID`),
  CONSTRAINT `workorder_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`),
  CONSTRAINT `workorder_ibfk_2` FOREIGN KEY (`vehicleID`) REFERENCES `vehicle` (`vehicleID`),
  CONSTRAINT `workorder_ibfk_3` FOREIGN KEY (`dealershipID`) REFERENCES `dealership` (`dealershipID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workOrder`
--

INSERT INTO `workOrder` VALUES (1,'2025-03-03',1,1,4,1),(2,'2025-03-03',1,2,5,1),(3,'2025-03-03',1,3,6,1);
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

--
-- View of dealerships with full addresses
--
CREATE VIEW vDealershipAddresses AS
SELECT dealershipID, address.streetAddress, city.cityName, county.countyName, state.stateName, address.ZIP
FROM dealership
INNER JOIN address ON dealership.addressID = address.addressID
INNER JOIN city ON address.cityID = city.cityID
INNER JOIN county ON city.countyID = county.countyID
INNER JOIN state ON county.stateID = state.stateID;


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-23 12:57:14
