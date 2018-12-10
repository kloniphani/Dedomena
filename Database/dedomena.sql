CREATE DATABASE  IF NOT EXISTS `dedomena` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
USE `dedomena`;
-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: dedomena
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `acceleration`
--

DROP TABLE IF EXISTS `acceleration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `acceleration` (
  `idacceleration` int(11) NOT NULL AUTO_INCREMENT,
  `x` float DEFAULT NULL,
  `y` float DEFAULT NULL,
  `z` float DEFAULT NULL,
  PRIMARY KEY (`idacceleration`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acceleration`
--

LOCK TABLES `acceleration` WRITE;
/*!40000 ALTER TABLE `acceleration` DISABLE KEYS */;
/*!40000 ALTER TABLE `acceleration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `device`
--

DROP TABLE IF EXISTS `device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `device` (
  `iddevice` int(11) NOT NULL AUTO_INCREMENT,
  `macAddress` varchar(45) NOT NULL,
  `manufacturer` varchar(45) DEFAULT NULL,
  `model` varchar(45) DEFAULT NULL,
  `firmware` varchar(45) DEFAULT NULL,
  `platform` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`iddevice`,`macAddress`),
  UNIQUE KEY `macaddress_UNIQUE` (`macAddress`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device`
--

LOCK TABLES `device` WRITE;
/*!40000 ALTER TABLE `device` DISABLE KEYS */;
/*!40000 ALTER TABLE `device` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gyroscope`
--

DROP TABLE IF EXISTS `gyroscope`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `gyroscope` (
  `idgyroscope` int(11) NOT NULL AUTO_INCREMENT,
  `pitch` float DEFAULT NULL,
  `roll` float DEFAULT NULL,
  `yaw` float DEFAULT NULL,
  PRIMARY KEY (`idgyroscope`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gyroscope`
--

LOCK TABLES `gyroscope` WRITE;
/*!40000 ALTER TABLE `gyroscope` DISABLE KEYS */;
/*!40000 ALTER TABLE `gyroscope` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sensor`
--

DROP TABLE IF EXISTS `sensor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `sensor` (
  `idsensor` int(11) NOT NULL AUTO_INCREMENT,
  `pressure` float DEFAULT NULL,
  `temperature` float DEFAULT NULL,
  `humidity` float DEFAULT NULL,
  `acceleration` int(11) DEFAULT NULL,
  `gyroscope` int(11) DEFAULT NULL,
  `magnetometer` float DEFAULT NULL,
  `timestamp` int(11) DEFAULT NULL,
  `deviceMacAddress` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idsensor`),
  KEY `sensorTimestamp_idx` (`timestamp`),
  KEY `deviceSensor_idx` (`deviceMacAddress`),
  KEY `sensorAcceleration_idx` (`acceleration`),
  KEY `sensorGyroscope_idx` (`gyroscope`),
  CONSTRAINT `deviceSensor` FOREIGN KEY (`deviceMacAddress`) REFERENCES `device` (`macaddress`),
  CONSTRAINT `sensorAcceleration` FOREIGN KEY (`acceleration`) REFERENCES `acceleration` (`idacceleration`),
  CONSTRAINT `sensorGyroscope` FOREIGN KEY (`gyroscope`) REFERENCES `gyroscope` (`idgyroscope`),
  CONSTRAINT `sensorTimestamp` FOREIGN KEY (`timestamp`) REFERENCES `timestamp` (`idtimestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensor`
--

LOCK TABLES `sensor` WRITE;
/*!40000 ALTER TABLE `sensor` DISABLE KEYS */;
/*!40000 ALTER TABLE `sensor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timestamp`
--

DROP TABLE IF EXISTS `timestamp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `timestamp` (
  `idtimestamp` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` varchar(45) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `zone` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idtimestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timestamp`
--

LOCK TABLES `timestamp` WRITE;
/*!40000 ALTER TABLE `timestamp` DISABLE KEYS */;
/*!40000 ALTER TABLE `timestamp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `traffic`
--

DROP TABLE IF EXISTS `traffic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `traffic` (
  `idtraffic` int(11) NOT NULL AUTO_INCREMENT,
  `deviceMacAddress` varchar(45) DEFAULT NULL,
  `flow` json DEFAULT NULL,
  `incidents` json DEFAULT NULL,
  `tiles` json DEFAULT NULL,
  `timestamp` int(11) DEFAULT NULL,
  PRIMARY KEY (`idtraffic`),
  KEY `deviceTraffic_idx` (`deviceMacAddress`),
  KEY `trafficTimestamp_idx` (`timestamp`),
  CONSTRAINT `deviceTraffic` FOREIGN KEY (`deviceMacAddress`) REFERENCES `device` (`macaddress`),
  CONSTRAINT `trafficTimestamp` FOREIGN KEY (`timestamp`) REFERENCES `timestamp` (`idtimestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `traffic`
--

LOCK TABLES `traffic` WRITE;
/*!40000 ALTER TABLE `traffic` DISABLE KEYS */;
/*!40000 ALTER TABLE `traffic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weather`
--

DROP TABLE IF EXISTS `weather`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `weather` (
  `idweather` int(11) NOT NULL,
  `timestamp` int(11) DEFAULT NULL,
  `daylight` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `skyInfo` varchar(45) DEFAULT NULL,
  `skyDescription` varchar(45) DEFAULT NULL,
  `temperature` varchar(45) DEFAULT NULL,
  `temperatureDesc` varchar(45) DEFAULT NULL,
  `comfort` varchar(45) DEFAULT NULL,
  `highTemperature` varchar(45) DEFAULT NULL,
  `lowTemperature` varchar(45) DEFAULT NULL,
  `humidity` varchar(45) DEFAULT NULL,
  `dewPoint` varchar(45) DEFAULT NULL,
  `precipitation1H` varchar(45) DEFAULT NULL,
  `precipitation3H` varchar(45) DEFAULT NULL,
  `precipitation6H` varchar(45) DEFAULT NULL,
  `precipitation12H` varchar(45) DEFAULT NULL,
  `precipitation24H` varchar(45) DEFAULT NULL,
  `precipitationDesc` varchar(45) DEFAULT NULL,
  `airInfo` varchar(45) DEFAULT NULL,
  `airDescription` varchar(45) DEFAULT NULL,
  `windSpeed` varchar(45) DEFAULT NULL,
  `windDirection` varchar(45) DEFAULT NULL,
  `windDesc` varchar(45) DEFAULT NULL,
  `windDescShort` varchar(45) DEFAULT NULL,
  `barometerPressure` varchar(45) DEFAULT NULL,
  `barometerTrend` varchar(45) DEFAULT NULL,
  `visibility` varchar(45) DEFAULT NULL,
  `snowCover` varchar(45) DEFAULT NULL,
  `icon` varchar(45) DEFAULT NULL,
  `iconName` varchar(45) DEFAULT NULL,
  `iconLink` varchar(45) DEFAULT NULL,
  `ageMinutes` varchar(45) DEFAULT NULL,
  `activeAlerts` varchar(45) DEFAULT NULL,
  `country` varchar(45) DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  `distance` float DEFAULT NULL,
  `elevation` varchar(45) DEFAULT NULL,
  `feedCreation` varchar(45) DEFAULT NULL,
  `deviceMacAddress` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idweather`),
  KEY `device_idx` (`deviceMacAddress`),
  KEY `wetherTimestamp_idx` (`timestamp`),
  CONSTRAINT `deviceWeather` FOREIGN KEY (`deviceMacAddress`) REFERENCES `device` (`macaddress`),
  CONSTRAINT `wetherTimestamp` FOREIGN KEY (`timestamp`) REFERENCES `timestamp` (`idtimestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weather`
--

LOCK TABLES `weather` WRITE;
/*!40000 ALTER TABLE `weather` DISABLE KEYS */;
/*!40000 ALTER TABLE `weather` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'dedomena'
--

--
-- Dumping routines for database 'dedomena'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-10 12:17:13
