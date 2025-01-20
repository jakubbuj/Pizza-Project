-- MySQL dump 10.13  Distrib 9.0.1, for macos14.4 (arm64)
--
-- Host: localhost    Database: piz
-- ------------------------------------------------------
-- Server version	9.0.1

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
-- Table structure for table `customer_info`
--

DROP TABLE IF EXISTS `customer_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_info` (
  `customer_id` int NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `phonenumber` int DEFAULT NULL,
  `streetname` varchar(100) DEFAULT NULL,
  `streetnumber` int DEFAULT NULL,
  `zipcode` varchar(10) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `birthdate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_info`
--

LOCK TABLES `customer_info` WRITE;
/*!40000 ALTER TABLE `customer_info` DISABLE KEYS */;
INSERT INTO `customer_info` VALUES (1,'Sample Customer',583890774,'Maple Street',5,'123456','M',NULL),(2,'OLAF',98678654,'Maasweg',78,'98725','male',NULL),(3,'OLAF',987567345,'Masweeg',89,'9876','Male',NULL),(4,'OLAF',987567543,'Maasweeg',98,'987','Male',NULL),(5,'OLAF',987456345,'Ifynkojdfydfitf',78,'87654','Male',NULL),(6,'OLAF',789567456,'Ifynkojdfidfitf',98,'98745','male',NULL),(7,'OLAF',789567345,'AJFYNKOJDFYFITF',67,'946','male',NULL),(8,'OLAF',768456372,'AJFYNKAJFDFYFDITF',76,'9867','male',NULL),(9,'OLAF',678456356,'OJFYNKOJFYDFITF',67,'6798','male',NULL),(10,'OLAF',765456873,'OJFYNKDFYDFITFF',67,'987','male',NULL),(11,'OLAF',765456278,'OJFYNKOJFDFYFDYTF',87,'987','male',NULL),(12,'OLAF',98745634,'OJFYNKOJFDYDFYTF',98,'987','male',NULL),(13,'OLAF',76534567,'OJFYNKOJFDYDFYTF',97,'9876','male',NULL),(14,'OLAF',987456356,'OJFYNKOJFDYDFYTF',98,'8765','male',NULL),(15,'OLAF',9876543,'OJFYNKOJFDFYDFYT',0,'5678','male','2003-09-26'),(16,'OLAF',678567456,'OJFYNKAJDFYFDFYT',98,'9876','male','2004-09-27'),(17,'nn',5,'e',3,'4','m','2003-09-27'),(18,'OLAF',789567456,'AJDONFYNK',87,'98','male','2003-09-27'),(19,'olaaaa',34,'e',2,'65432','male','2003-10-21'),(19,'kaska',2,'d',2,'98765','dem','2003-10-21'),(19,'misia',23,'d',1,'12345','demo','2003-10-21'),(19,'misia',3,'d',2,'21098','pan','2003-10-21'),(19,'misia',2,'d',1,'12345','demo','2003-10-21'),(19,'hugo',3,'s',2,'21098','male','2003-10-21'),(19,'olek',2,'d',1,'98765','pan','2003-10-21'),(19,'wiktor',3,'s',1,'54321','male','2003-10-21'),(19,'kuba',3,'hg',2,'90876','d','2003-10-21'),(19,'d',2,'d',2,'10987','d','2003-10-21'),(19,'olka',3,'d',7,'90876','g','2003-10-21'),(19,'d',2,'d',5,'10987','g','2003-10-21'),(19,'Nia',2,'ff',2,'12345','f','2003-10-21'),(19,'doris',2,'d',1,'12345','f','2003-10-21'),(19,'dorissss',2,'r',2,'54321','r','2003-10-21'),(19,'ola',2,'d',2,'98765','f','2003-10-21'),(19,'nyn',2,'d',3,'43210','f','2003-10-21'),(19,'nyn',2,'d',3,'43210','f','2003-10-21'),(19,'nina',345,'f',2,'32109','d','2003-10-21'),(19,'olkka',2,'d',2,'90876','d','2003-10-21'),(19,'ewkaa',2,'d',4,'10987','female police officeer','2003-10-21'),(19,'Nina',4567890,'df',2,'21098','male','2003-10-21'),(19,'olkamorelka',3,'d',2,'43210','nonbinary','2003-10-21'),(19,'jakub',3456,'gee',54,'65432','male','2003-10-21'),(19,'olka r',3,'d',4,'54321','femalemale','2003-10-21'),(19,'olka oreka',2345,'df',4,'12345','pan','2003-10-21'),(19,'arika',45678,'deoje',22,'12345','fem','2003-10-21'),(19,'olka',23,'d',3,'12345','d','2003-10-21'),(19,'jdh',3,'d',2,'12345','c','2003-10-21'),(19,'nij',3,'d',2,'12345','c','2003-10-21'),(19,'nin',23,'d',2,'12345','d','2003-10-21'),(19,'ola',3,'d',3,'12345','d','2003-10-21'),(19,'olk',2,'d',2,'54321','d','2003-10-21'),(19,'nuna',2,'d',2,'54321','d','2003-10-21'),(19,'s',2,'d',3,'54321','d','2003-10-21'),(19,'d',3,'d',3,'54321','d','2003-10-21'),(19,'no',2,'d',1,'54321','d','2003-10-21'),(19,'nun',2,'d',2,'90876','d','2003-10-21'),(19,'jk',3,'e',3,'90876','d','2003-10-21'),(19,'f',3,'d',3,'90876','f','2003-10-21'),(19,'f',3,'d',3,'90876','d','2003-10-21'),(19,'fghj',2,'e',2,'90876','d','2003-10-21'),(19,'d',3,'d',3,'90876','d','2003-10-21'),(19,'d',3,'d',3,'90876','d','2003-10-21'),(19,'d',3,'f',3,'12345','v','2003-10-21'),(19,'d',3,'d',3,'12345','d','2003-10-21'),(19,'df',7,'j',9,'12345','h','2003-10-21'),(20,'Ula Sawczuk',897654736,'ferr',2,'10987','female','2003-10-07');
/*!40000 ALTER TABLE `customer_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deliveryperson`
--

DROP TABLE IF EXISTS `deliveryperson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deliveryperson` (
  `deliveryperson_id` int NOT NULL AUTO_INCREMENT,
  `birthdate` date DEFAULT NULL,
  `phonenumber` bigint DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `zip_code` varchar(10) DEFAULT NULL,
  `is_available` tinyint(1) DEFAULT '1',
  `unavailable_until` datetime DEFAULT NULL,
  PRIMARY KEY (`deliveryperson_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deliveryperson`
--

LOCK TABLES `deliveryperson` WRITE;
/*!40000 ALTER TABLE `deliveryperson` DISABLE KEYS */;
INSERT INTO `deliveryperson` VALUES (1,'2003-10-03',678567456,'John Doe',NULL,1,NULL),(2,'2000-09-24',679245160,'John Doe',NULL,1,NULL),(3,'1995-12-01',678123456,'Alice Smith','12345',1,NULL),(4,'1998-05-15',679876543,'Bob Johnson','54321',1,NULL),(5,'1990-11-22',678987654,'Charlie Brown','98765',1,NULL),(6,'1985-03-30',679564321,'David White','87654',1,NULL),(7,'1992-07-14',678234567,'Eva Green','65432',1,NULL),(8,'1989-02-10',678987321,'Frank Black','43210',1,NULL),(9,'1991-06-25',679432156,'George Blue','32109',1,NULL),(10,'1993-09-18',678765432,'Hannah Yellow','21098',1,NULL),(11,'1987-12-07',679543210,'Irene Red','10987',0,'2024-10-07 12:17:31'),(12,'1994-04-05',678345678,'Jack Gray','90876',1,NULL),(13,'1990-05-15',678111111,'Linda White','12345',1,NULL),(14,'1994-07-22',678222222,'Michael Brown','54321',1,NULL),(15,'1988-11-05',678333333,'Nancy Black','98765',1,NULL),(16,'1995-02-19',678444444,'Oscar Blue','87654',1,NULL),(17,'1991-08-30',678555555,'Paula Green','65432',1,NULL),(18,'1993-09-10',678666666,'Quincy Red','43210',1,NULL),(19,'1985-04-01',678777777,'Rachel Gray','32109',1,NULL),(20,'1992-12-25',678888888,'Sam Smith','21098',1,NULL),(21,'1990-06-14',678999999,'Tina Yellow','10987',1,NULL),(22,'1987-03-11',679000000,'Ursula Orange','90876',1,NULL);
/*!40000 ALTER TABLE `deliveryperson` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dessert`
--

DROP TABLE IF EXISTS `dessert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dessert` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dessert`
--

LOCK TABLES `dessert` WRITE;
/*!40000 ALTER TABLE `dessert` DISABLE KEYS */;
INSERT INTO `dessert` VALUES (1,'Brownie',5.99),(2,'Cheesecake',3.49),(3,'Tiramisu',7.00);
/*!40000 ALTER TABLE `dessert` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DessertOrders`
--

DROP TABLE IF EXISTS `DessertOrders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DessertOrders` (
  `order_number` int NOT NULL,
  `dessert_id` int NOT NULL,
  PRIMARY KEY (`order_number`,`dessert_id`),
  KEY `dessert_id` (`dessert_id`),
  CONSTRAINT `dessertorders_ibfk_1` FOREIGN KEY (`order_number`) REFERENCES `Orders` (`order_number`),
  CONSTRAINT `dessertorders_ibfk_2` FOREIGN KEY (`dessert_id`) REFERENCES `Dessert` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DessertOrders`
--

LOCK TABLES `DessertOrders` WRITE;
/*!40000 ALTER TABLE `DessertOrders` DISABLE KEYS */;
INSERT INTO `DessertOrders` VALUES (105,1),(104,2),(107,2);
/*!40000 ALTER TABLE `DessertOrders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discount`
--

DROP TABLE IF EXISTS `discount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `discount` (
  `discount_id` int NOT NULL AUTO_INCREMENT,
  `discount_code` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`discount_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discount`
--

LOCK TABLES `discount` WRITE;
/*!40000 ALTER TABLE `discount` DISABLE KEYS */;
INSERT INTO `discount` VALUES (1,'No-dis'),(5,'BIRTHDAY'),(6,'SUMMER2024'),(7,'STUDENT'),(8,'NO_D');
/*!40000 ALTER TABLE `discount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drink`
--

DROP TABLE IF EXISTS `drink`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drink` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drink`
--

LOCK TABLES `drink` WRITE;
/*!40000 ALTER TABLE `drink` DISABLE KEYS */;
INSERT INTO `drink` VALUES (1,'Coke',1.99),(2,'Sprite',1.99),(3,'Lemonade',2.49),(4,'Water',0.99),(5,'Orange juice',3.00);
/*!40000 ALTER TABLE `drink` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DrinkOrders`
--

DROP TABLE IF EXISTS `DrinkOrders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DrinkOrders` (
  `drink_id` int NOT NULL,
  `order_number` int NOT NULL,
  PRIMARY KEY (`drink_id`,`order_number`),
  KEY `order_number` (`order_number`),
  CONSTRAINT `drinkorders_ibfk_1` FOREIGN KEY (`drink_id`) REFERENCES `Drink` (`id`),
  CONSTRAINT `drinkorders_ibfk_2` FOREIGN KEY (`order_number`) REFERENCES `Orders` (`order_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DrinkOrders`
--

LOCK TABLES `DrinkOrders` WRITE;
/*!40000 ALTER TABLE `DrinkOrders` DISABLE KEYS */;
INSERT INTO `DrinkOrders` VALUES (2,19),(4,20),(5,20),(1,23),(5,38),(4,42),(2,43),(3,43),(5,43),(5,103),(1,104),(1,107),(3,107),(5,109),(4,124);
/*!40000 ALTER TABLE `DrinkOrders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingredient`
--

DROP TABLE IF EXISTS `ingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredient` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(25) DEFAULT NULL,
  `cost` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredient`
--

LOCK TABLES `ingredient` WRITE;
/*!40000 ALTER TABLE `ingredient` DISABLE KEYS */;
INSERT INTO `ingredient` VALUES (1,'Tomato Sauce',1.00),(2,'Mozzarella',1.50),(3,'Pepperoni',2.75),(4,'BBQ Sauce',1.20),(5,'Chicken',3.25),(6,'Bell Peppers',1.10),(7,'Pineapple',2.50),(8,'Ham',2.30),(9,'Bacon',2.40),(10,'Onions',0.90),(11,'Jalapenos',1.15),(12,'Pesto Sauce',1.75),(13,'Feta Cheese',2.10),(14,'Cheddar',1.80),(15,'Mushrooms',1.25),(16,'Sausage',2.60),(17,'Olives',1.05),(18,'Parmesan',2.20);
/*!40000 ALTER TABLE `ingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `numberforpizzas`
--

DROP TABLE IF EXISTS `numberforpizzas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `numberforpizzas` (
  `customer_id` int NOT NULL,
  `number_of_pizzas` int DEFAULT '0',
  PRIMARY KEY (`customer_id`),
  CONSTRAINT `fk_customer` FOREIGN KEY (`customer_id`) REFERENCES `Registration` (`customer_id`) ON DELETE CASCADE,
  CONSTRAINT `fk_numberforpizzas_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `registration` (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `numberforpizzas`
--

LOCK TABLES `numberforpizzas` WRITE;
/*!40000 ALTER TABLE `numberforpizzas` DISABLE KEYS */;
INSERT INTO `numberforpizzas` VALUES (5,33),(17,2),(18,2),(19,46),(20,1);
/*!40000 ALTER TABLE `numberforpizzas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderconfirmation`
--

DROP TABLE IF EXISTS `orderconfirmation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orderconfirmation` (
  `order_number` int NOT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `order_price` decimal(10,2) DEFAULT NULL,
  `estimate_time` time DEFAULT NULL,
  `discount_used` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`order_number`),
  CONSTRAINT `orderconfirmation_ibfk_1` FOREIGN KEY (`order_number`) REFERENCES `Orders` (`order_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderconfirmation`
--

LOCK TABLES `orderconfirmation` WRITE;
/*!40000 ALTER TABLE `orderconfirmation` DISABLE KEYS */;
INSERT INTO `orderconfirmation` VALUES (32,'2024-09-26','17:40:12',7.00,'00:00:30',0),(33,'2024-09-26','17:42:36',9.00,'00:00:30',0),(34,'2024-09-26','17:52:05',8.00,'00:00:30',0),(35,'2024-09-26','17:59:02',6.00,'00:00:30',0),(36,'2024-09-26','18:00:14',7.00,'00:00:30',0),(37,'2024-09-26','18:02:46',6.00,'00:00:30',0),(38,'2024-09-26','18:05:38',9.00,'00:00:30',0),(39,'2024-09-26','18:09:16',23.00,'00:00:30',0),(40,'2024-09-26','18:10:11',7.00,'00:00:30',0),(41,'2024-09-27','13:03:03',0.00,'00:00:30',0),(42,'2024-09-27','13:42:57',16.00,'00:00:30',1),(43,'2024-09-27','13:56:09',12.00,'00:00:30',0),(44,'2024-09-27','14:31:59',7.00,'00:00:30',0),(45,'2024-09-27','14:36:02',7.00,'00:00:30',0),(46,'2024-09-27','14:41:03',7.00,'00:00:30',0),(47,'2024-09-27','14:44:19',7.00,'00:00:30',0),(48,'2024-09-27','14:47:17',7.60,'00:00:30',0),(49,'2024-09-27','20:28:54',7.40,'00:00:30',0),(50,'2024-09-27','23:27:52',6.90,'00:00:30',0),(51,'2024-09-28','11:33:27',NULL,'00:00:30',0),(52,'2024-09-28','12:08:53',NULL,'00:00:30',0),(53,'2024-09-28','12:20:31',NULL,'00:00:30',0),(54,'2024-09-28','12:34:21',NULL,'00:00:30',0),(55,'2024-09-28','12:37:42',NULL,'00:00:30',0),(56,'2024-09-28','12:40:37',16.80,'00:00:30',0),(57,'2024-09-29','14:02:04',7.70,'00:00:30',0),(58,'2024-09-29','16:30:34',7.70,'00:00:30',0),(59,'2024-09-29','17:05:05',15.29,'00:00:30',0),(60,'2024-09-29','17:07:11',13.60,'00:00:30',0),(66,'2024-09-30','12:55:11',14.10,'00:00:30',0),(67,'2024-09-30','12:59:29',7.60,'00:00:30',0),(68,'2024-09-30','13:03:30',6.50,'00:00:30',0),(69,'2024-09-30','13:06:25',5.90,'00:00:30',0),(70,'2024-09-30','13:09:10',15.30,'00:00:30',0),(71,'2024-09-30','13:35:51',7.40,'00:00:30',0),(72,'2024-09-30','13:38:03',7.70,'00:00:30',0),(73,'2024-09-30','13:42:46',5.90,'00:00:30',0),(74,'2024-09-30','13:46:05',7.70,'00:00:30',0),(75,'2024-09-30','13:47:07',7.60,'00:00:30',0),(76,'2024-09-30','13:49:18',5.90,'00:00:30',0),(77,'2024-09-30','13:51:00',7.60,'00:00:30',0),(78,'2024-09-30','13:52:09',7.70,'00:00:30',0),(79,'2024-09-30','13:55:10',8.50,'00:00:30',0),(80,'2024-09-30','13:57:25',6.70,'00:00:30',0),(81,'2024-09-30','14:00:29',5.90,'00:00:30',0),(82,'2024-09-30','14:02:34',7.70,'00:00:30',0),(83,'2024-10-05','20:50:12',8.50,'00:00:30',0),(84,'2024-10-05','21:32:53',5.50,'00:00:30',0),(85,'2024-10-05','21:41:24',6.90,'00:00:30',0),(86,'2024-10-05','22:01:22',7.70,'00:00:30',0),(87,'2024-10-05','22:04:09',14.70,'00:00:30',0),(88,'2024-10-05','22:05:16',8.90,'00:00:30',0),(89,'2024-10-05','22:06:07',6.70,'00:00:30',0),(90,'2024-10-05','22:09:03',5.90,'00:00:30',0),(91,'2024-10-05','22:24:01',7.60,'00:00:30',0),(92,'2024-10-05','22:26:44',7.70,'00:00:30',0),(93,'2024-10-05','22:33:56',6.90,'00:00:30',0),(99,'2024-10-05','23:03:05',8.50,'00:00:30',0),(100,'2024-10-06','14:13:20',15.90,'00:00:30',0),(103,'2024-10-06','14:54:55',20.70,'00:00:30',0),(104,'2024-10-06','14:57:02',23.78,'00:00:30',0),(105,'2024-10-06','15:01:05',31.29,'00:00:30',1),(106,'2024-10-06','15:03:59',7.40,'00:00:30',1),(109,'2024-10-06','21:45:34',17.30,'00:00:30',0),(110,'2024-10-06','21:46:15',7.60,'00:00:30',0),(111,'2024-10-06','21:46:47',7.40,'00:00:30',0),(112,'2024-10-06','21:47:14',7.60,'00:00:30',0),(113,'2024-10-06','21:47:42',8.50,'00:00:30',0),(114,'2024-10-06','21:48:14',7.40,'00:00:30',1),(115,'2024-10-06','21:55:07',7.60,'00:00:30',0),(116,'2024-10-06','21:55:30',7.60,'00:00:30',0),(117,'2024-10-06','21:56:31',6.50,'00:00:30',0),(118,'2024-10-06','21:57:03',7.40,'00:00:30',0),(119,'2024-10-06','22:00:28',6.50,'00:00:30',0),(120,'2024-10-06','22:17:22',7.40,'00:00:30',0),(121,'2024-10-06','22:17:47',7.40,'00:00:30',0),(122,'2024-10-06','22:18:30',9.20,'00:00:30',1),(123,'2024-10-06','22:19:03',5.90,'00:00:30',0),(124,'2024-10-06','22:19:31',7.49,'00:00:30',0);
/*!40000 ALTER TABLE `orderconfirmation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_number` int NOT NULL AUTO_INCREMENT,
  `customer_id` int DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `order_price` decimal(10,2) DEFAULT NULL,
  `discount_id` int DEFAULT '1',
  `deliveryperson_id` int DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`order_number`),
  KEY `customer_id` (`customer_id`),
  KEY `discount_id` (`discount_id`),
  KEY `fk_deliveryperson` (`deliveryperson_id`),
  CONSTRAINT `fk_deliveryperson` FOREIGN KEY (`deliveryperson_id`) REFERENCES `Deliveryperson` (`deliveryperson_id`),
  CONSTRAINT `fk_orders_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `registration` (`customer_id`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`discount_id`) REFERENCES `discount` (`discount_id`)
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,1,'2024-09-23','16:47:14',26.00,NULL,NULL,NULL),(2,1,'2024-09-24','23:32:35',13.00,NULL,NULL,NULL),(17,NULL,'2024-09-26','13:56:04',12.00,1,1,NULL),(18,5,'2024-09-26','14:55:52',9.00,1,1,NULL),(19,5,'2024-09-26','16:10:05',15.00,1,1,NULL),(20,5,'2024-09-26','16:16:09',30.00,1,1,NULL),(21,5,'2024-09-26','16:35:04',30.00,7,1,NULL),(22,5,'2024-09-26','16:37:06',20.00,1,1,NULL),(23,5,'2024-09-26','17:00:39',15.00,1,1,NULL),(24,5,'2024-09-26','17:09:08',8.00,1,1,NULL),(25,5,'2024-09-26','17:15:55',6.00,1,1,NULL),(26,5,'2024-09-26','17:19:36',8.00,1,1,NULL),(27,5,'2024-09-26','17:22:34',9.00,1,1,NULL),(28,5,'2024-09-26','17:27:29',8.00,1,1,NULL),(29,5,'2024-09-26','17:31:26',7.00,1,1,NULL),(30,5,'2024-09-26','17:37:51',7.00,1,1,NULL),(31,5,'2024-09-26','17:38:51',9.00,1,1,NULL),(32,5,'2024-09-26','17:40:11',7.00,1,1,NULL),(33,5,'2024-09-26','17:42:36',9.00,1,1,NULL),(34,5,'2024-09-26','17:52:05',8.00,1,1,NULL),(35,5,'2024-09-26','17:59:02',6.00,1,1,NULL),(36,5,'2024-09-26','18:00:14',7.00,1,1,NULL),(37,5,'2024-09-26','18:02:46',6.00,1,1,NULL),(38,5,'2024-09-26','18:05:38',9.00,1,1,NULL),(39,5,'2024-09-26','18:09:16',23.00,1,1,NULL),(40,5,'2024-09-26','18:10:11',7.00,1,1,NULL),(41,17,'2024-09-27','13:03:02',0.00,1,1,NULL),(42,17,'2024-09-27','13:42:57',16.00,7,1,NULL),(43,18,'2024-09-27','13:56:09',12.00,1,1,NULL),(44,18,'2024-09-27','14:31:59',7.00,1,1,NULL),(45,18,'2024-09-27','14:36:02',7.40,1,1,NULL),(46,18,'2024-09-27','14:41:03',7.40,1,1,NULL),(47,18,'2024-09-27','14:44:19',7.40,1,1,NULL),(48,18,'2024-09-27','14:47:17',7.60,1,1,NULL),(49,18,'2024-09-27','20:28:54',7.40,1,1,NULL),(50,18,'2024-09-27','23:27:52',6.90,1,3,NULL),(51,18,'2024-09-28','11:33:27',NULL,1,13,NULL),(52,18,'2024-09-28','12:08:53',NULL,1,3,NULL),(53,18,'2024-09-28','12:20:31',NULL,1,3,NULL),(54,18,'2024-09-28','12:34:21',NULL,1,3,NULL),(55,18,'2024-09-28','12:37:42',NULL,1,4,NULL),(56,18,'2024-09-28','12:40:37',16.80,1,5,NULL),(57,18,'2024-09-29','14:02:04',7.70,1,15,NULL),(58,18,'2024-09-29','16:30:34',7.70,1,3,NULL),(59,18,'2024-09-29','17:05:05',15.29,1,8,NULL),(60,18,'2024-09-29','17:07:11',13.60,1,6,NULL),(66,18,'2024-09-30','12:55:11',14.10,1,15,NULL),(67,18,'2024-09-30','12:59:29',7.60,1,7,NULL),(68,18,'2024-09-30','13:03:30',6.50,1,6,NULL),(69,18,'2024-09-30','13:06:25',5.90,1,17,NULL),(70,18,'2024-09-30','13:09:10',15.30,1,16,NULL),(71,18,'2024-09-30','13:35:51',7.40,1,6,NULL),(72,18,'2024-09-30','13:38:03',7.70,1,4,NULL),(73,18,'2024-09-30','13:42:46',5.90,1,10,NULL),(74,18,'2024-09-30','13:46:05',7.70,1,16,NULL),(75,18,'2024-09-30','13:47:07',7.60,1,7,NULL),(76,18,'2024-09-30','13:49:18',5.90,1,14,NULL),(77,18,'2024-09-30','13:51:00',7.60,1,5,NULL),(78,18,'2024-09-30','13:52:09',7.70,1,15,'In Process'),(79,18,'2024-09-30','13:55:10',8.50,1,3,'In Process'),(80,18,'2024-09-30','13:57:25',6.70,1,20,'In Process'),(81,18,'2024-09-30','14:00:29',5.90,1,11,'In Process'),(82,18,'2024-09-30','14:02:34',7.70,1,21,'Out for Delivery'),(83,18,'2024-10-05','20:50:12',8.50,1,3,'In Process'),(84,19,'2024-10-05','21:32:53',5.50,1,3,'In Process'),(85,19,'2024-10-05','21:41:24',6.90,1,8,'In Process'),(86,19,'2024-10-05','22:01:22',7.70,1,5,NULL),(87,19,'2024-10-05','22:04:09',14.70,1,4,NULL),(88,19,'2024-10-05','22:05:16',8.90,1,7,NULL),(89,19,'2024-10-05','22:06:07',6.70,1,15,NULL),(90,19,'2024-10-05','22:09:03',5.90,1,3,'In Process'),(91,19,'2024-10-05','22:24:01',7.60,1,10,NULL),(92,19,'2024-10-05','22:26:43',7.70,1,13,NULL),(93,19,'2024-10-05','22:33:56',6.90,1,20,NULL),(99,19,'2024-10-05','23:03:04',8.50,1,21,NULL),(100,19,'2024-10-06','14:13:20',15.90,1,3,NULL),(103,19,'2024-10-06','14:54:55',20.70,1,12,NULL),(104,19,'2024-10-06','14:57:02',23.78,1,11,NULL),(105,19,'2024-10-06','15:01:05',31.29,7,10,NULL),(106,19,'2024-10-06','15:03:59',7.40,6,8,NULL),(107,19,'2024-10-06','15:09:55',45.06,1,7,'In Process'),(109,19,'2024-10-06','21:45:34',17.30,1,3,NULL),(110,19,'2024-10-06','21:46:15',7.60,1,13,NULL),(111,19,'2024-10-06','21:46:47',7.40,1,3,NULL),(112,19,'2024-10-06','21:47:14',7.60,1,3,NULL),(113,19,'2024-10-06','21:47:42',8.50,1,13,NULL),(114,19,'2024-10-06','21:48:14',7.40,6,13,NULL),(115,19,'2024-10-06','21:55:07',7.60,1,4,NULL),(116,19,'2024-10-06','21:55:30',7.60,1,4,NULL),(117,19,'2024-10-06','21:56:31',6.50,1,4,NULL),(118,19,'2024-10-06','21:57:03',7.40,1,14,NULL),(119,19,'2024-10-06','22:00:28',6.50,1,14,NULL),(120,19,'2024-10-06','22:17:22',7.40,1,12,NULL),(121,19,'2024-10-06','22:17:47',7.40,1,12,NULL),(122,19,'2024-10-06','22:18:30',9.20,6,22,NULL),(123,19,'2024-10-06','22:19:03',5.90,1,22,NULL),(124,19,'2024-10-06','22:19:31',7.49,1,22,NULL);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pizza`
--

DROP TABLE IF EXISTS `Pizza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Pizza` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(25) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `is_vegetarian` tinyint(1) DEFAULT NULL,
  `is_vegan` tinyint(1) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pizza`
--

LOCK TABLES `Pizza` WRITE;
/*!40000 ALTER TABLE `Pizza` DISABLE KEYS */;
INSERT INTO `Pizza` VALUES (1,'Margherita','Tomato Sauce, Mozzarella',1,0,5.50),(2,'Pepperoni','Tomato Sauce, Mozzarella, Pepperoni',0,0,6.70),(3,'BBQ Chicken','Mozzarella, BBQ Sauce, Chicken, Onions',0,0,7.70),(4,'Vegetarian','Tomato Sauce, Mozzarella, Bell Peppers, Onions, Cheddar',1,0,5.90),(5,'Hawaiian','Tomato Sauce, Mozzarella, Pineapple, Ham',0,0,6.90),(6,'Meat Lovers','Tomato Sauce, Mozzarella, Pepperoni, Chicken, Bacon, Mushrooms',0,0,8.50),(7,'Buffalo Chicken','Mozzarella, BBQ Sauce, Chicken, Onions',0,0,7.60),(8,'Pesto Veggie','Bell Peppers, Onions, Pesto Sauce, Feta Cheese',1,0,6.50),(9,'Four Cheese','Mozzarella, Feta Cheese, Cheddar, Parmesan',1,0,7.40),(10,'Supreme','Tomato Sauce, Mozzarella, Pepperoni, Bell Peppers, Bacon, Onions, Mushrooms, Sausage',0,0,9.20);
/*!40000 ALTER TABLE `Pizza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PizzaIngredient`
--

DROP TABLE IF EXISTS `PizzaIngredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PizzaIngredient` (
  `pizza_id` int NOT NULL,
  `ingredient_id` int NOT NULL,
  PRIMARY KEY (`pizza_id`,`ingredient_id`),
  KEY `ingredient_id` (`ingredient_id`),
  CONSTRAINT `pizzaingredient_ibfk_1` FOREIGN KEY (`pizza_id`) REFERENCES `Pizza` (`id`),
  CONSTRAINT `pizzaingredient_ibfk_2` FOREIGN KEY (`ingredient_id`) REFERENCES `Ingredient` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PizzaIngredient`
--

LOCK TABLES `PizzaIngredient` WRITE;
/*!40000 ALTER TABLE `PizzaIngredient` DISABLE KEYS */;
INSERT INTO `PizzaIngredient` VALUES (1,1),(2,1),(4,1),(5,1),(6,1),(10,1),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(9,2),(10,2),(2,3),(6,3),(10,3),(3,4),(7,4),(3,5),(6,5),(7,5),(4,6),(8,6),(10,6),(5,7),(5,8),(6,9),(10,9),(3,10),(4,10),(7,10),(8,10),(10,10),(8,12),(8,13),(9,13),(4,14),(9,14),(6,15),(10,15),(10,16),(9,18);
/*!40000 ALTER TABLE `PizzaIngredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pizzaorders`
--

DROP TABLE IF EXISTS `pizzaorders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pizzaorders` (
  `pizza_id` int NOT NULL,
  `order_number` int NOT NULL,
  `quantity` int DEFAULT '1',
  PRIMARY KEY (`pizza_id`,`order_number`),
  KEY `order_number` (`order_number`),
  CONSTRAINT `pizzaorders_ibfk_1` FOREIGN KEY (`pizza_id`) REFERENCES `Pizza` (`id`),
  CONSTRAINT `pizzaorders_ibfk_2` FOREIGN KEY (`order_number`) REFERENCES `Orders` (`order_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pizzaorders`
--

LOCK TABLES `pizzaorders` WRITE;
/*!40000 ALTER TABLE `pizzaorders` DISABLE KEYS */;
INSERT INTO `pizzaorders` VALUES (1,17,1),(1,20,1),(2,22,1),(2,30,1),(2,42,1),(3,22,1),(3,24,1),(3,28,1),(3,34,1),(3,39,1),(4,19,1),(4,21,1),(4,22,1),(4,23,1),(4,25,1),(4,35,1),(4,37,1),(4,38,1),(4,43,1),(4,104,1),(4,105,3),(4,107,3),(4,123,1),(5,17,1),(5,29,1),(5,32,1),(5,36,1),(5,40,1),(5,109,1),(6,18,1),(6,27,1),(6,31,1),(6,33,1),(6,42,1),(6,103,1),(6,107,1),(6,113,1),(7,19,1),(7,20,1),(7,23,1),(7,26,1),(7,105,1),(7,110,1),(7,112,1),(7,115,1),(7,116,1),(8,104,1),(8,117,1),(8,119,1),(8,124,1),(9,20,1),(9,43,1),(9,106,1),(9,107,1),(9,109,1),(9,111,1),(9,114,1),(9,118,1),(9,120,1),(9,121,1),(10,103,1),(10,122,1);
/*!40000 ALTER TABLE `pizzaorders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pricecalculation`
--

DROP TABLE IF EXISTS `pricecalculation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pricecalculation` (
  `pizza_id` int NOT NULL,
  `ingredient_cost_sum` decimal(8,2) DEFAULT NULL,
  `profit_margin` decimal(5,2) DEFAULT NULL,
  `vat` decimal(5,2) DEFAULT NULL,
  `final_price` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`pizza_id`),
  CONSTRAINT `pricecalculation_ibfk_1` FOREIGN KEY (`pizza_id`) REFERENCES `Pizza` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pricecalculation`
--

LOCK TABLES `pricecalculation` WRITE;
/*!40000 ALTER TABLE `pricecalculation` DISABLE KEYS */;
INSERT INTO `pricecalculation` VALUES (1,2.50,2.00,1.00,5.50),(2,3.00,2.50,1.20,6.70),(3,3.50,2.80,1.40,7.70),(4,2.80,2.00,1.10,5.90),(5,3.20,2.40,1.30,6.90),(6,4.00,3.00,1.50,8.50),(7,3.50,2.70,1.40,7.60),(8,3.00,2.20,1.30,6.50),(9,3.50,2.60,1.30,7.40),(10,4.50,3.00,1.70,9.20);
/*!40000 ALTER TABLE `pricecalculation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registration`
--

DROP TABLE IF EXISTS `registration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registration` (
  `username` varchar(20) DEFAULT NULL,
  `passkey` varchar(255) DEFAULT NULL,
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `birthdate` date DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registration`
--

LOCK TABLES `registration` WRITE;
/*!40000 ALTER TABLE `registration` DISABLE KEYS */;
INSERT INTO `registration` VALUES ('hello1234','hello1234',1,NULL),('hello123','hello123',2,NULL),('nina','1234',3,NULL),('ninaaa','333',4,NULL),('nin','$2b$12$B.wrum4hIJLp80/nkgXk0.6pGuUwjnrZR4tzo.Mu2GoVJsuPaTcRe',5,NULL),('robert','$2b$12$PEqNo.vRKAeRqh51d9q27e/0qyJPmff2pgNQcW2.WVwF4TNAWE5wi',6,NULL),('robey','$2b$12$lmj9Z3azXKZ.n4qGJuvC/uWaeXytD1txF0xDSw4tzWCQH2U1I6tfu',7,NULL),('roby','$2b$12$kO8ghQM.Dg6XxC5DbK.Zh.sGEf2kR56wPKWyGoKnrXXVfTreIkNn2',8,NULL),('tobi','$2b$12$eHG3.bOs876WmN2X0v1cc.fE14nd6ia9FUoTom1QujQMPhmP1PBPa',9,NULL),('jh','$2b$12$cv/BTIgamgmvJ86gCJ1PuOQERcEkWYq4MloWthRNPUAEYezDL2kXa',10,NULL),('olaf','$2b$12$5quRGwd1recTjsZqrVPVaeotJWioIHfeNI.hKxU1N7VQnH5V/Mehy',11,NULL),('r','$2b$12$CiPeDV9rLp3u5I4otspBEuPSIMwMA4HxEgBjpjO6e9jn.VcxlUvqG',12,NULL),('hgf','$2b$12$dNqu1KUUXPk3nCD5kE3CmuAbTOo7Dd9NJ2P8Eecq/BToIlAL.a/V.',13,NULL),('uro','$2b$12$sMMAVazn6JPOxUaerVnn3OnP4Gkg3voQzVSvlgUXnrNst8LehpIRe',14,NULL),('yolo','$2b$12$4lznmMICVpnWYUNv4rztXOwMfiqLBkwxccGa/iH8yYGGQ9yaAOEOK',15,'2003-09-26'),('me','$2b$12$uKk7zR4CQeblcLgpEIdrV.CiMEfjQ3MHRFzAcmFrMaAc8rxxOcspW',16,'2004-09-27'),('kuba','$2b$12$8Y8mfb7M74bpOSkXAwXr4u3EMpcAQStjz4qpBbFXodqfbsB7eEhDG',17,'2003-09-27'),('nina123','$2b$12$cJv5YwLJGtT6lmcUPJUKfuglYdTBGlATc/12QJINwBORwqpTBP9ie',18,'2003-09-27'),('nyna','$2b$12$Me7s.3nhV40pg17md4kB/.jbmRtxFutEjzMZz2RgriM4rEo/RDrJm',19,'2003-10-21'),('ula','$2b$12$aUaguRRY0KLtRudvhLDA/utt/0n8qNCzFXOhJnSuJb7wGtZMCCXJq',20,'2003-10-07');
/*!40000 ALTER TABLE `registration` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-08 21:50:24
