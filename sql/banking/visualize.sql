-- MySQL dump 10.13  Distrib 5.1.73, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: banking
-- ------------------------------------------------------
-- Server version	5.1.73

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Account`
--

DROP TABLE IF EXISTS `Account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Account` (
  `AccountID` int(11) NOT NULL AUTO_INCREMENT,
  `AccountName` varchar(50) NOT NULL,
  `AccountAllocation` float NOT NULL,
  `AccountBalance` float NOT NULL,
  `Type` varchar(10) NOT NULL,
  `Description` varchar(150) NOT NULL,
  `Created` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `Updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`AccountID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `AccountTransaction`
--

DROP TABLE IF EXISTS `AccountTransaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AccountTransaction` (
  `TransactionID` int(11) NOT NULL AUTO_INCREMENT,
  `AccountID` int(11) NOT NULL,
  `AllocatedOn` datetime NOT NULL,
  `NewAccountAllocation` float NOT NULL,
  `isActive` tinyint(1) NOT NULL,
  `AccountMetadata` blob NOT NULL,
  `Created` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `Updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`TransactionID`),
  KEY `AccountTransaction_fk0` (`AccountID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Job`
--

DROP TABLE IF EXISTS `Job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Job` (
  `JobNumber` bigint(20) NOT NULL AUTO_INCREMENT,
  `JobSlurmID` int(11) NOT NULL,
  `SubmitDate` datetime NOT NULL,
  `StartDate` datetime NOT NULL,
  `EndDate` datetime NOT NULL,
  `UserID` int(11) NOT NULL,
  `AccountID` int(11) NOT NULL,
  `Amount` float NOT NULL,
  `JobStatus` tinyint(4) NOT NULL,
  `Partition` tinyint(4) NOT NULL,
  `QOS` smallint(6) NOT NULL,
  `Created` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `Updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`JobNumber`),
  KEY `Job_fk0` (`UserID`),
  KEY `Job_fk1` (`AccountID`),
  KEY `Job_fk2` (`JobStatus`),
  KEY `Job_fk3` (`Partition`),
  KEY `Job_fk4` (`QOS`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `JobStatusDict`
--

DROP TABLE IF EXISTS `JobStatusDict`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `JobStatusDict` (
  `JobStatus` tinyint(4) NOT NULL AUTO_INCREMENT,
  `Description` varchar(150) NOT NULL,
  `Created` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `Updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`JobStatus`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `PartitionDict`
--

DROP TABLE IF EXISTS `PartitionDict`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PartitionDict` (
  `Partition` tinyint(4) NOT NULL AUTO_INCREMENT,
  `Description` varchar(150) NOT NULL,
  `Created` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `Updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`Partition`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `PermDict`
--

DROP TABLE IF EXISTS `PermDict`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PermDict` (
  `Perm` int(11) NOT NULL AUTO_INCREMENT,
  `Description` varchar(150) NOT NULL,
  `Created` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `Updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`Perm`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `QOSDict`
--

DROP TABLE IF EXISTS `QOSDict`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `QOSDict` (
  `QOS` smallint(6) NOT NULL AUTO_INCREMENT,
  `Description` varchar(150) NOT NULL,
  `Created` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `Updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`QOS`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Role`
--

DROP TABLE IF EXISTS `Role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Role` (
  `AccountID` int(11) NOT NULL DEFAULT '0',
  `UserID` int(11) NOT NULL DEFAULT '0',
  `Permission` tinyint(4) DEFAULT NULL,
  `Created` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `Updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`AccountID`,`UserID`),
  KEY `Role_fk1` (`UserID`),
  KEY `Role_fk2` (`Permission`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `RoleDict`
--

DROP TABLE IF EXISTS `RoleDict`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RoleDict` (
  `Role` tinyint(4) NOT NULL AUTO_INCREMENT,
  `Perm` int(11) NOT NULL,
  `Created` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `Updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`Role`),
  KEY `RoleDict_fk0` (`Perm`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `SuperUser`
--

DROP TABLE IF EXISTS `SuperUser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SuperUser` (
  `UserID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `LDAPUID` int(11) NOT NULL,
  `Created` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `Updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`UserID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `UserID` int(11) NOT NULL AUTO_INCREMENT,
  `UserName` varchar(20) NOT NULL,
  `UserMetadata` blob NOT NULL,
  `Email` varchar(100) NOT NULL,
  `LDAPUID` int(11) NOT NULL,
  `Created` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `Updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`UserID`),
  UNIQUE KEY `UserID` (`UserID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `UserAccountAssociation`
--

DROP TABLE IF EXISTS `UserAccountAssociation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UserAccountAssociation` (
  `UserID` int(11) NOT NULL AUTO_INCREMENT,
  `AccountID` int(11) NOT NULL,
  `UserAllocation` float NOT NULL,
  `UserBalance` float NOT NULL,
  `Created` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `Updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`UserID`,`AccountID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-08-03 15:01:58
