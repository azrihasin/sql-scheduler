SELECT * FROM student WHERE email='ahmad@gmail.com' AND password='1234';
SELECT matricno FROM student WHERE email='ahmad@gmail.com' AND password='1234';
INSERT INTO student VALUES ('1123444', 'yusi', 'yusi@gmail.com','7788', 'kemns');
INSERT INTO student VALUES ('2478888', 'ahma', 'ahma@gmail.com','1234', 'kict');
UPDATE student SET studentname='aliy',
email='ali@yahoo.com', password='9999', kuliyyah='kenms'
WHERE matricno='1234567';
DELETE FROM student WHERE matricno='1621111';

SELECT * FROM place WHERE placeid='2';
SELECT placelevel, placeblock FROM student WHERE placename='lab 6';
INSERT INTO place VALUES('50', 'lab 20', 5, 'c');
INSERT INTO place VALUES('45', 'lab 30', 3, 'd');
UPDATE place SET placename='lab 12', placeblock='b', placelevel=2
WHERE placeid='4';
DELETE FROM place WHERE placeid='10';

SELECT * FROM subject WHERE coursecode='CSC 1100';
SELECT subjectname FROM subject WHERE coursecode='INFO 1500';
INSERT INTO subject VALUES('CSC 1100', 'element of programming 2', 3, '2');
INSERT INTO subject VALUES('CSC 1200', 'object oriented programming 2', 3, '1');
UPDATE subject SET subjectname='data structures',
placeid='60' WHERE coursecode='INFO 1500';
DELETE FROM subject WHERE coursecode='INFOM 1500';

SELECT * FROM schedule WHERE matricno='1812129';
SELECT starttime, endtime, day FROM schedule WHERE matricno='1812133';
INSERT INTO schedule VALUES('1030', '1230', 'tuesday', '1812129', 'CSC 1100');
INSERT INTO schedule VALUES('1400', '1520', 'wednesday','1812131', 'CSC 1100');
UPDATE schedule  SET starttime='1145', endtime='1300',
day='sunday', coursecode='INFO 1500'
WHERE matricno='1234567';
DELETE FROM schedule WHERE matricno='1621111';