/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - online_health
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`online_health` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `online_health`;

/*Table structure for table `disease` */

DROP TABLE IF EXISTS `disease`;

CREATE TABLE `disease` (
  `diseaseid` int(30) NOT NULL AUTO_INCREMENT,
  `disease` varchar(40) DEFAULT NULL,
  `details` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`diseaseid`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `disease` */

insert  into `disease`(`diseaseid`,`disease`,`details`) values (5,'covid19','dfghgfd'),(2,'covid19','headache');

/*Table structure for table `doctor` */

DROP TABLE IF EXISTS `doctor`;

CREATE TABLE `doctor` (
  `doctorid` int(30) NOT NULL AUTO_INCREMENT,
  `loginid` int(30) DEFAULT NULL,
  `firstname` varchar(40) DEFAULT NULL,
  `lastname` varchar(20) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  `place` varchar(60) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `qualification` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`doctorid`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `doctor` */

insert  into `doctor`(`doctorid`,`loginid`,`firstname`,`lastname`,`image`,`place`,`phone`,`email`,`qualification`) values (6,13,'Aswani','M','static/4330f029-4f3b-4f20-a2f9-5789440998a1addition.PNG','asxdcv','8086388815','aswaniramachandran@gmail.com','as'),(9,16,'abeel','a','static/6201608f-9bbf-4799-8fbb-b737826f9adcpb bg.jpg','kochi','955458545','abeel@gmail.com','mbbs,md(surgeon)'),(8,15,'asd','asad','static/46018ad8-12f6-4c70-8518-5927051773b5pb bg.jpg','dssdsd','69879666666','asd@dddf','aasds');

/*Table structure for table `doctorhospital` */

DROP TABLE IF EXISTS `doctorhospital`;

CREATE TABLE `doctorhospital` (
  `dhospital_id` int(11) NOT NULL AUTO_INCREMENT,
  `doctorid` int(11) DEFAULT NULL,
  `hospitalid` int(11) DEFAULT NULL,
  PRIMARY KEY (`dhospital_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `doctorhospital` */

/*Table structure for table `hospital` */

DROP TABLE IF EXISTS `hospital`;

CREATE TABLE `hospital` (
  `hospitalid` int(30) NOT NULL AUTO_INCREMENT,
  `loginid` int(30) DEFAULT NULL,
  `hname` varchar(40) DEFAULT NULL,
  `place` varchar(40) DEFAULT NULL,
  `phone` varchar(40) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `link` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`hospitalid`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `hospital` */

insert  into `hospital`(`hospitalid`,`loginid`,`hname`,`place`,`phone`,`email`,`link`) values (2,7,'jkj','ljihugj','18086388815','aswanimnbr@gmail.com','aaqsxdfvg');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `loginid` int(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`loginid`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'Aswani','asdxcf','user'),(3,'Aswani','asdxcf','user'),(4,'admin','Aswani','hospital'),(5,'admin','Ammu123','hospital'),(6,'admin','Aswani','hospital'),(7,'jjked4r','nnee','hospital'),(13,'admin','Aswani','doctor'),(9,'admin','admin','doctor'),(16,'abc','aswani','doctor'),(15,'pp','pp','doctor');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `requestid` int(30) NOT NULL AUTO_INCREMENT,
  `userid` int(30) DEFAULT NULL,
  `doctorid` int(30) DEFAULT NULL,
  `result` varchar(30) DEFAULT NULL,
  `date` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`requestid`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `request` */

/*Table structure for table `specialists` */

DROP TABLE IF EXISTS `specialists`;

CREATE TABLE `specialists` (
  `specialistid` int(30) NOT NULL AUTO_INCREMENT,
  `doctorid` int(30) DEFAULT NULL,
  `diseaseid` int(30) DEFAULT NULL,
  PRIMARY KEY (`specialistid`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `specialists` */

insert  into `specialists`(`specialistid`,`doctorid`,`diseaseid`) values (1,2,2);

/*Table structure for table `symptoms` */

DROP TABLE IF EXISTS `symptoms`;

CREATE TABLE `symptoms` (
  `symptomsid` int(40) NOT NULL AUTO_INCREMENT,
  `diseaseid` int(30) DEFAULT NULL,
  `symptoms` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`symptomsid`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `symptoms` */

insert  into `symptoms`(`symptomsid`,`diseaseid`,`symptoms`) values (1,2,'sssss'),(2,2,'vvvv'),(3,5,'sssss');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `userid` int(30) NOT NULL AUTO_INCREMENT,
  `loginid` int(30) DEFAULT NULL,
  `firstname` varchar(50) DEFAULT NULL,
  `lastname` varchar(50) DEFAULT NULL,
  `place` varchar(40) DEFAULT NULL,
  `phone` varchar(40) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`userid`,`loginid`,`firstname`,`lastname`,`place`,`phone`,`email`) values (1,3,'Aswani','M','asxdcv','18086388815','aswanimnbr@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
