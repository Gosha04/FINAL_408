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
CREATE TABLE `address` (
  `addressID` int NOT NULL AUTO_INCREMENT,
  `streetAddress` varchar(70) NOT NULL,
  `ZIP` varchar(5) NOT NULL,
  `cityID` int NOT NULL,
  PRIMARY KEY (`addressID`),
  KEY `cityID` (`cityID`),
  CONSTRAINT `address_ibfk_1` FOREIGN KEY (`cityID`) REFERENCES `city` (`cityID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--


--
-- Table structure for table `city`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `city` (
  `cityID` int NOT NULL AUTO_INCREMENT,
  `cityName` varchar(20) NOT NULL,
  `countyID` int NOT NULL,
  PRIMARY KEY (`cityID`),
  KEY `countyID` (`countyID`),
  CONSTRAINT `city_ibfk_1` FOREIGN KEY (`countyID`) REFERENCES `county` (`countyID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `city`
--


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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `county`
--


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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--


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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dealership`
--


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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--


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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rental`
--


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
  PRIMARY KEY (`saleID`),
  KEY `employeeID` (`employeeID`),
  KEY `customerID` (`customerID`),
  KEY `dealershipID` (`dealershipID`),
  CONSTRAINT `sale_ibfk_1` FOREIGN KEY (`employeeID`) REFERENCES `employee` (`employeeID`),
  CONSTRAINT `sale_ibfk_2` FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerID`),
  CONSTRAINT `sale_ibfk_3` FOREIGN KEY (`dealershipID`) REFERENCES `dealership` (`dealershipID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sale`
--


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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `state`
--


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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicle`
--


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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workOrder`
--

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-22  9:07:47
