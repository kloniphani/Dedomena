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
) ENGINE=InnoDB AUTO_INCREMENT=349 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device`
--

LOCK TABLES `device` WRITE;
/*!40000 ALTER TABLE `device` DISABLE KEYS */;
INSERT INTO `device` VALUES (224,'B8-27-EB-49-F5-75','Raspberry Pi','Model B+',NULL,NULL);
/*!40000 ALTER TABLE `device` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `geolocation`
--

DROP TABLE IF EXISTS `geolocation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `geolocation` (
  `idgeolocation` int(11) NOT NULL AUTO_INCREMENT,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  `altitude` float DEFAULT NULL,
  `accuracy` float DEFAULT NULL,
  `heading` float DEFAULT NULL,
  `speed` float DEFAULT NULL,
  `altitudeAccuracy` double DEFAULT NULL,
  PRIMARY KEY (`idgeolocation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `geolocation`
--

LOCK TABLES `geolocation` WRITE;
/*!40000 ALTER TABLE `geolocation` DISABLE KEYS */;
/*!40000 ALTER TABLE `geolocation` ENABLE KEYS */;
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
  `geolocation` int(11) DEFAULT NULL,
  PRIMARY KEY (`idsensor`),
  KEY `sensorTimestamp_idx` (`timestamp`),
  KEY `deviceSensor_idx` (`deviceMacAddress`),
  KEY `sensorAcceleration_idx` (`acceleration`),
  KEY `sensorGyroscope_idx` (`gyroscope`),
  KEY `sensorGeolocation_idx` (`geolocation`),
  CONSTRAINT `deviceSensor` FOREIGN KEY (`deviceMacAddress`) REFERENCES `device` (`macaddress`),
  CONSTRAINT `sensorAcceleration` FOREIGN KEY (`acceleration`) REFERENCES `acceleration` (`idacceleration`),
  CONSTRAINT `sensorGeolocation` FOREIGN KEY (`geolocation`) REFERENCES `geolocation` (`idgeolocation`),
  CONSTRAINT `sensorGyroscope` FOREIGN KEY (`gyroscope`) REFERENCES `gyroscope` (`idgyroscope`),
  CONSTRAINT `sensorTimestamp` FOREIGN KEY (`timestamp`) REFERENCES `timestamp` (`idtimestamp`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensor`
--

LOCK TABLES `sensor` WRITE;
/*!40000 ALTER TABLE `sensor` DISABLE KEYS */;
INSERT INTO `sensor` VALUES (1,965.794,33.6902,41.4455,NULL,NULL,NULL,NULL,'B8-27-EB-49-F5-75',NULL),(2,965.762,33.7085,43.628,NULL,NULL,NULL,NULL,'B8-27-EB-49-F5-75',NULL),(3,965.767,33.7085,44.9407,NULL,NULL,NULL,NULL,'B8-27-EB-49-F5-75',NULL),(4,965.767,33.7996,42.9183,NULL,NULL,NULL,NULL,'B8-27-EB-49-F5-75',NULL),(5,965.753,33.7267,43.3367,NULL,NULL,NULL,NULL,'B8-27-EB-49-F5-75',NULL),(6,965.755,33.7085,44.3213,NULL,NULL,NULL,NULL,'B8-27-EB-49-F5-75',NULL),(7,965.774,33.7085,43.4803,NULL,NULL,NULL,NULL,'B8-27-EB-49-F5-75',NULL),(8,965.794,33.6173,43.8946,NULL,NULL,NULL,NULL,'B8-27-EB-49-F5-75',NULL),(9,965.787,33.7814,44.4238,NULL,NULL,NULL,NULL,'B8-27-EB-49-F5-75',NULL),(10,965.79,33.7085,43.628,NULL,NULL,NULL,NULL,'B8-27-EB-49-F5-75',NULL),(11,965.763,33.7632,43.8905,NULL,NULL,NULL,NULL,'B8-27-EB-49-F5-75',NULL),(12,965.779,33.7267,43.829,NULL,NULL,NULL,55,'B8-27-EB-49-F5-75',NULL),(13,965.769,33.7814,43.829,NULL,NULL,NULL,56,'B8-27-EB-49-F5-75',NULL),(14,965.792,33.6902,43.4557,NULL,NULL,NULL,57,'B8-27-EB-49-F5-75',NULL),(15,965.793,33.7814,44.67,NULL,NULL,NULL,58,'B8-27-EB-49-F5-75',NULL),(16,965.793,33.7996,44.0874,NULL,NULL,NULL,59,'B8-27-EB-49-F5-75',NULL),(17,965.796,33.6538,43.788,NULL,NULL,NULL,60,'B8-27-EB-49-F5-75',NULL),(18,965.758,33.6355,43.3531,NULL,NULL,NULL,61,'B8-27-EB-49-F5-75',NULL),(19,965.767,33.7632,43.7223,NULL,NULL,NULL,62,'B8-27-EB-49-F5-75',NULL),(20,965.779,33.7632,45.0228,NULL,NULL,NULL,63,'B8-27-EB-49-F5-75',NULL),(21,965.843,33.8361,43.39,NULL,NULL,NULL,64,'B8-27-EB-49-F5-75',NULL),(22,965.762,33.7085,43.7552,NULL,NULL,NULL,65,'B8-27-EB-49-F5-75',NULL),(23,965.813,33.6902,43.8577,NULL,NULL,NULL,66,'B8-27-EB-49-F5-75',NULL),(24,965.827,33.8179,42.9388,NULL,NULL,NULL,67,'B8-27-EB-49-F5-75',NULL),(25,965.792,33.7449,44.0546,NULL,NULL,NULL,68,'B8-27-EB-49-F5-75',NULL),(26,965.807,33.7085,43.9316,NULL,NULL,NULL,69,'B8-27-EB-49-F5-75',NULL),(27,965.821,33.7632,43.8003,NULL,NULL,NULL,70,'B8-27-EB-49-F5-75',NULL),(28,965.809,33.7996,44.0915,NULL,NULL,NULL,71,'B8-27-EB-49-F5-75',NULL),(29,965.766,33.6902,43.8946,NULL,NULL,NULL,72,'B8-27-EB-49-F5-75',NULL),(30,965.803,33.6173,45.1089,NULL,NULL,NULL,73,'B8-27-EB-49-F5-75',NULL),(31,965.788,33.6902,43.669,NULL,NULL,NULL,74,'B8-27-EB-49-F5-75',NULL),(32,965.776,33.7449,43.8987,NULL,NULL,NULL,75,'B8-27-EB-49-F5-75',NULL),(33,965.757,33.6902,43.669,NULL,NULL,NULL,76,'B8-27-EB-49-F5-75',NULL),(34,965.703,33.7085,43.8618,NULL,NULL,NULL,77,'B8-27-EB-49-F5-75',NULL),(35,965.708,33.8361,43.911,NULL,NULL,NULL,78,'B8-27-EB-49-F5-75',NULL),(36,965.72,33.672,44.0423,NULL,NULL,NULL,79,'B8-27-EB-49-F5-75',NULL),(37,965.714,33.7632,41.4168,NULL,NULL,NULL,80,'B8-27-EB-49-F5-75',NULL),(38,965.7,33.6355,44.0628,NULL,NULL,NULL,81,'B8-27-EB-49-F5-75',NULL),(39,965.699,33.6538,43.7346,NULL,NULL,NULL,82,'B8-27-EB-49-F5-75',NULL),(40,965.724,33.8726,43.9562,NULL,NULL,NULL,83,'B8-27-EB-49-F5-75',NULL),(41,965.711,33.8361,43.6198,NULL,NULL,NULL,84,'B8-27-EB-49-F5-75',NULL),(42,965.715,33.7449,43.8864,NULL,NULL,NULL,85,'B8-27-EB-49-F5-75',NULL),(43,965.73,33.8179,44.3336,NULL,NULL,NULL,86,'B8-27-EB-49-F5-75',NULL),(44,965.701,33.8543,46.0402,NULL,NULL,NULL,87,'B8-27-EB-49-F5-75',NULL),(45,965.724,33.7996,44.0423,NULL,NULL,NULL,88,'B8-27-EB-49-F5-75',NULL),(46,965.734,33.7814,43.0126,NULL,NULL,NULL,89,'B8-27-EB-49-F5-75',NULL),(47,965.792,33.7632,43.9193,NULL,NULL,NULL,90,'B8-27-EB-49-F5-75',NULL),(48,965.77,33.7085,44.03,NULL,NULL,NULL,91,'B8-27-EB-49-F5-75',NULL),(49,965.757,33.8179,44.0628,NULL,NULL,NULL,92,'B8-27-EB-49-F5-75',NULL),(50,965.788,33.9637,43.7305,NULL,NULL,NULL,93,'B8-27-EB-49-F5-75',NULL),(51,965.792,33.909,43.8372,NULL,NULL,NULL,94,'B8-27-EB-49-F5-75',NULL),(52,965.776,33.9273,43.7346,NULL,NULL,NULL,95,'B8-27-EB-49-F5-75',NULL),(53,965.777,33.8543,44.0915,NULL,NULL,NULL,96,'B8-27-EB-49-F5-75',NULL),(54,965.794,33.7632,44.0423,NULL,NULL,NULL,97,'B8-27-EB-49-F5-75',NULL),(55,965.737,33.8726,43.8536,NULL,NULL,NULL,98,'B8-27-EB-49-F5-75',NULL),(56,965.772,33.8726,43.7839,NULL,NULL,NULL,99,'B8-27-EB-49-F5-75',NULL),(57,965.749,33.8361,44.4361,NULL,NULL,NULL,100,'B8-27-EB-49-F5-75',NULL),(58,965.831,33.9273,43.7921,NULL,NULL,NULL,101,'B8-27-EB-49-F5-75',NULL),(59,965.722,33.7996,44.0956,NULL,NULL,NULL,102,'B8-27-EB-49-F5-75',NULL),(60,965.759,33.8908,43.9069,NULL,NULL,NULL,103,'B8-27-EB-49-F5-75',NULL),(61,965.735,33.7996,44.0587,NULL,NULL,NULL,104,'B8-27-EB-49-F5-75',NULL),(62,965.754,33.8908,44.1203,NULL,NULL,NULL,105,'B8-27-EB-49-F5-75',NULL);
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
  `date` varchar(45) DEFAULT NULL,
  `time` varchar(45) DEFAULT NULL,
  `zone` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idtimestamp`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timestamp`
--

LOCK TABLES `timestamp` WRITE;
/*!40000 ALTER TABLE `timestamp` DISABLE KEYS */;
INSERT INTO `timestamp` VALUES (1,NULL,'14/12/2018','15:18:58',NULL),(2,NULL,'14/12/2018','15:19:09',NULL),(3,NULL,'14/12/2018','15:19:20',NULL),(4,NULL,'14/12/2018','15:19:30',NULL),(5,NULL,'14/12/2018','15:19:40',NULL),(6,NULL,'14/12/2018','15:22:02',NULL),(7,NULL,'14/12/2018','15:22:13',NULL),(8,NULL,'14/12/2018','15:22:24',NULL),(9,NULL,'14/12/2018','15:22:34',NULL),(10,NULL,'14/12/2018','15:22:44',NULL),(11,NULL,'14/12/2018','15:22:55',NULL),(12,NULL,'14/12/2018','15:23:05',NULL),(13,NULL,'14/12/2018','15:23:16',NULL),(14,NULL,'14/12/2018','15:23:26',NULL),(15,NULL,'14/12/2018','15:23:36',NULL),(16,NULL,'14/12/2018','15:23:47',NULL),(17,NULL,'14/12/2018','15:23:57',NULL),(18,NULL,'14/12/2018','15:24:08',NULL),(19,NULL,'14/12/2018','15:24:18',NULL),(20,NULL,'14/12/2018','15:24:28',NULL),(21,NULL,'14/12/2018','15:24:39',NULL),(22,NULL,'14/12/2018','15:24:49',NULL),(23,NULL,'14/12/2018','15:25:00',NULL),(24,NULL,'14/12/2018','15:25:10',NULL),(25,NULL,'14/12/2018','15:25:20',NULL),(26,NULL,'14/12/2018','15:25:31',NULL),(27,NULL,'14/12/2018','15:25:41',NULL),(28,NULL,'14/12/2018','15:25:52',NULL),(29,NULL,'14/12/2018','15:26:02',NULL),(30,NULL,'14/12/2018','15:26:14',NULL),(31,NULL,'14/12/2018','15:26:24',NULL),(32,NULL,'14/12/2018','15:26:34',NULL),(33,NULL,'14/12/2018','15:26:45',NULL),(34,NULL,'14/12/2018','15:26:55',NULL),(35,NULL,'14/12/2018','15:27:05',NULL),(36,NULL,'14/12/2018','15:27:16',NULL),(37,NULL,'14/12/2018','15:27:26',NULL),(38,NULL,'14/12/2018','15:27:52',NULL),(39,NULL,'14/12/2018','15:28:02',NULL),(40,NULL,'14/12/2018','15:28:13',NULL),(41,NULL,'14/12/2018','15:28:23',NULL),(42,NULL,'14/12/2018','15:28:34',NULL),(43,NULL,'14/12/2018','15:28:44',NULL),(44,NULL,'14/12/2018','15:31:01',NULL),(45,NULL,'14/12/2018','15:31:12',NULL),(46,NULL,'14/12/2018','15:31:23',NULL),(47,NULL,'14/12/2018','15:31:33',NULL),(48,NULL,'14/12/2018','15:31:44',NULL),(49,NULL,'14/12/2018','15:31:54',NULL),(50,NULL,'14/12/2018','15:32:05',NULL),(51,NULL,'14/12/2018','15:32:15',NULL),(52,NULL,'14/12/2018','15:32:25',NULL),(53,NULL,'14/12/2018','15:32:36',NULL),(54,NULL,'14/12/2018','15:32:46',NULL),(55,NULL,'14/12/2018','15:33:02',NULL),(56,NULL,'14/12/2018','15:33:13',NULL),(57,NULL,'14/12/2018','15:33:23',NULL),(58,NULL,'14/12/2018','15:33:34',NULL),(59,NULL,'14/12/2018','15:33:44',NULL),(60,NULL,'14/12/2018','15:33:55',NULL),(61,NULL,'14/12/2018','15:34:05',NULL),(62,NULL,'14/12/2018','15:34:16',NULL),(63,NULL,'14/12/2018','15:34:26',NULL),(64,NULL,'14/12/2018','15:34:37',NULL),(65,NULL,'14/12/2018','15:34:47',NULL),(66,NULL,'14/12/2018','15:34:57',NULL),(67,NULL,'14/12/2018','15:35:08',NULL),(68,NULL,'14/12/2018','15:35:18',NULL),(69,NULL,'14/12/2018','15:35:29',NULL),(70,NULL,'14/12/2018','15:35:39',NULL),(71,NULL,'14/12/2018','15:35:50',NULL),(72,NULL,'14/12/2018','15:36:00',NULL),(73,NULL,'14/12/2018','15:36:10',NULL),(74,NULL,'14/12/2018','15:36:21',NULL),(75,NULL,'14/12/2018','15:36:31',NULL),(76,NULL,'14/12/2018','15:36:42',NULL),(77,NULL,'14/12/2018','15:36:52',NULL),(78,NULL,'14/12/2018','15:37:04',NULL),(79,NULL,'14/12/2018','15:37:30',NULL),(80,NULL,'14/12/2018','15:37:41',NULL),(81,NULL,'14/12/2018','15:37:51',NULL),(82,NULL,'14/12/2018','15:38:02',NULL),(83,NULL,'14/12/2018','15:38:12',NULL),(84,NULL,'14/12/2018','15:38:22',NULL),(85,NULL,'14/12/2018','15:38:33',NULL),(86,NULL,'14/12/2018','15:38:43',NULL),(87,NULL,'14/12/2018','15:38:54',NULL),(88,NULL,'14/12/2018','15:39:04',NULL),(89,NULL,'14/12/2018','15:39:15',NULL),(90,NULL,'14/12/2018','15:39:25',NULL),(91,NULL,'14/12/2018','15:39:35',NULL),(92,NULL,'14/12/2018','15:39:46',NULL),(93,NULL,'14/12/2018','15:39:56',NULL),(94,NULL,'14/12/2018','15:40:07',NULL),(95,NULL,'14/12/2018','15:40:17',NULL),(96,NULL,'14/12/2018','15:40:28',NULL),(97,NULL,'14/12/2018','15:40:38',NULL),(98,NULL,'14/12/2018','15:40:49',NULL),(99,NULL,'14/12/2018','15:40:59',NULL),(100,NULL,'14/12/2018','15:41:09',NULL),(101,NULL,'14/12/2018','15:41:20',NULL),(102,NULL,'14/12/2018','15:41:30',NULL),(103,NULL,'14/12/2018','15:41:41',NULL),(104,NULL,'14/12/2018','15:41:51',NULL),(105,NULL,'14/12/2018','15:42:01',NULL);
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

-- Dump completed on 2018-12-14 16:53:06
