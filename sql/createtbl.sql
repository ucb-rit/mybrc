SHOW DATABASES;
USE test;
CREATE TABLE `user` (`id` INT NOT NULL AUTO_INCREMENT,
                   `description` TINYBLOB,
                   PRIMARY KEY (`id`));
INSERT INTO user (description) VALUES ('shasan');
INSERT INTO user (description) VALUES ('kuoh');
INSERT INTO user (description) VALUES ('rmaneri');
SELECT * FROM user;
