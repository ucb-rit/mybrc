USE banking;

CREATE TABLE `User` (
	`UserID` int NOT NULL AUTO_INCREMENT UNIQUE,
	`UserName` varchar(20) NOT NULL,
	`UserMetadata` blob NOT NULL,
	`Email` varchar(100) NOT NULL,
	`LDAPUID` int NOT NULL,
	`Created` timestamp DEFAULT '0000-00-00 00:00:00',
	`Updated` timestamp DEFAULT now() ON UPDATE now(),
	PRIMARY KEY (`UserID`)
) ENGINE=INNODB;

CREATE TABLE `Account` (
        `AccountID` int NOT NULL AUTO_INCREMENT,
        `AccountName` varchar(50) NOT NULL,
        `AccountAllocation` int NOT NULL,
        `AccountBalance` int NOT NULL,
        `Type` varchar(10) NOT NULL,
        `Description` varchar(150) NOT NULL,
        `Created` timestamp DEFAULT '0000-00-00 00:00:00',
        `Updated` timestamp DEFAULT now() ON UPDATE now(),
        PRIMARY KEY (`AccountID`)
) ENGINE=INNODB;

CREATE TABLE `UserAccountAssociation` (
	`UserID` int NOT NULL,
	`AccountID` int NOT NULL,
	FOREIGN KEY (`UserID`) REFERENCES User(`UserID`),
	FOREIGN KEY (`AccountID`) REFERENCES `Account`(`AccountID`),
	`id` int NOT NULL AUTO_INCREMENT,
	`UserAllocation` int NOT NULL,
	`UserBalance` int NOT NULL,
	`Created` timestamp DEFAULT '0000-00-00 00:00:00', 
        `Updated` timestamp DEFAULT now() ON UPDATE now(),
	PRIMARY KEY (`id`)
) ENGINE=INNODB;

CREATE TABLE `JobStatusDict` (
	`JobStatus` tinyint NOT NULL AUTO_INCREMENT,
	`Description` varchar(150) NOT NULL,
	`Created` timestamp DEFAULT '0000-00-00 00:00:00', 
        `Updated` timestamp DEFAULT now() ON UPDATE now(),
	PRIMARY KEY (`JobStatus`)
) ENGINE=INNODB;

CREATE TABLE `PartitionDict` (
	`Partition` tinyint NOT NULL AUTO_INCREMENT,
	`Description` varchar(150) NOT NULL,
	`Created` timestamp DEFAULT '0000-00-00 00:00:00', 
        `Updated` timestamp DEFAULT now() ON UPDATE now(),
	PRIMARY KEY (`Partition`)
) ENGINE=INNODB;

CREATE TABLE `QOSDict` (
	`QOS` smallint NOT NULL AUTO_INCREMENT,
	`Description` varchar(150) NOT NULL,
	`Created` timestamp DEFAULT '0000-00-00 00:00:00', 
        `Updated` timestamp DEFAULT now() ON UPDATE now(),
	PRIMARY KEY (`QOS`)
) ENGINE=INNODB;

CREATE TABLE `RoleDict` (
	`Role` tinyint NOT NULL AUTO_INCREMENT,
	`Perm` int NOT NULL,
	`Created` timestamp DEFAULT '0000-00-00 00:00:00', 
        `Updated` timestamp DEFAULT now() ON UPDATE now(),
	PRIMARY KEY (`Role`)
) ENGINE=INNODB;

CREATE TABLE `SuperUser` (
	`UserID` int NOT NULL AUTO_INCREMENT,
	`Name` varchar(50) NOT NULL,
	`LDAPUID` int NOT NULL,
	`Created` timestamp DEFAULT '0000-00-00 00:00:00', 
        `Updated` timestamp DEFAULT now() ON UPDATE now(),
	PRIMARY KEY (`UserID`)
) ENGINE=INNODB;

CREATE TABLE `AccountTransaction` (
	`TransactionID` int NOT NULL AUTO_INCREMENT,
	`AccountID` int NOT NULL,
	`AllocatedOn` DATETIME NOT NULL,
	`NewAccountAllocation` FLOAT NOT NULL,
	`isActive` bool NOT NULL,
	`AccountMetadata` blob NOT NULL,
	`Created` timestamp DEFAULT '0000-00-00 00:00:00', 
        `Updated` timestamp DEFAULT now() ON UPDATE now(),
	PRIMARY KEY (`TransactionID`)
) ENGINE=INNODB;

CREATE TABLE `Job` (
	`JobNumber` bigint NOT NULL AUTO_INCREMENT,
	`JobSlurmID` int NOT NULL,
	`SubmitDate` DATETIME NOT NULL,
	`StartDate` DATETIME,
	`EndDate` DATETIME,
	`UserID` int NOT NULL,
	`AccountID` int NOT NULL,
	`Amount` FLOAT NOT NULL,
	`JobStatus` tinyint NOT NULL,
	`Partition` tinyint NOT NULL,
	`QOS` smallint NOT NULL,
	`Created` timestamp DEFAULT '0000-00-00 00:00:00', 
        `Updated` timestamp DEFAULT now() ON UPDATE now(),
	PRIMARY KEY (`JobNumber`)
) ENGINE=INNODB;

CREATE TABLE `Role` (
	`AccountID` int,
	`UserID` int,
	`Permission` tinyint,
	`Created` timestamp DEFAULT '0000-00-00 00:00:00', 
        `Updated` timestamp DEFAULT now() ON UPDATE now(),
	PRIMARY KEY (`AccountID`, `UserID`)
) ENGINE=INNODB;

CREATE TABLE `PermDict` (
	`Perm` int NOT NULL AUTO_INCREMENT,
	`Description` varchar(150) NOT NULL,
	`Created` timestamp DEFAULT '0000-00-00 00:00:00', 
        `Updated` timestamp DEFAULT now() ON UPDATE now(),
	PRIMARY KEY (`Perm`)
) ENGINE=INNODB;

ALTER TABLE `RoleDict` ADD CONSTRAINT `RoleDict_fk0` FOREIGN KEY (`Perm`) REFERENCES `PermDict`(`Perm`);

ALTER TABLE `AccountTransaction` ADD CONSTRAINT `AccountTransaction_fk0` FOREIGN KEY (`AccountID`) REFERENCES `Account`(`AccountID`);

ALTER TABLE `Job` ADD CONSTRAINT `Job_fk0` FOREIGN KEY (`UserID`) REFERENCES `User`(`UserID`);

ALTER TABLE `Job` ADD CONSTRAINT `Job_fk1` FOREIGN KEY (`AccountID`) REFERENCES `Account`(`AccountID`);

ALTER TABLE `Job` ADD CONSTRAINT `Job_fk2` FOREIGN KEY (`JobStatus`) REFERENCES `JobStatusDict`(`JobStatus`);

ALTER TABLE `Job` ADD CONSTRAINT `Job_fk3` FOREIGN KEY (`Partition`) REFERENCES `PartitionDict`(`Partition`);

ALTER TABLE `Job` ADD CONSTRAINT `Job_fk4` FOREIGN KEY (`QOS`) REFERENCES `QOSDict`(`QOS`);

ALTER TABLE `Role` ADD CONSTRAINT `Role_fk0` FOREIGN KEY (`AccountID`) REFERENCES `Account`(`AccountID`);

ALTER TABLE `Role` ADD CONSTRAINT `Role_fk1` FOREIGN KEY (`UserID`) REFERENCES `User`(`UserID`);

ALTER TABLE `Role` ADD CONSTRAINT `Role_fk2` FOREIGN KEY (`Permission`) REFERENCES `RoleDict`(`Role`);

SHOW TABLES;
