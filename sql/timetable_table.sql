DROP TABLE schedule;
DROP TABLE subject;
DROP TABLE place;
DROP TABLE student;

CREATE TABLE student (
                matricno VARCHAR2(8) NOT NULL,
                studentname VARCHAR2(25) NOT NULL,
                email VARCHAR2(25) NOT NULL,
                password VARCHAR2(25) NOT NULL,
                kulliyyah VARCHAR2(30),
                PRIMARY KEY (matricno)
            );

CREATE TABLE place(
                placeID VARCHAR2(15) NOT NULL,
                placename VARCHAR2(25) NOT NULL,
                placelevel NUMBER(2),
                placeblock VARCHAR2(2),
                PRIMARY KEY (placeID)
            );

CREATE TABLE subject(
                coursecode VARCHAR2(12) NOT NULL,
                subjectname VARCHAR2(25) NOT NULL,
                credithour NUMBER(2),
                PRIMARY KEY (coursecode),
                placeID VARCHAR2(15),
                FOREIGN KEY(placeID) REFERENCES place(placeID) ON DELETE CASCADE
            );

CREATE TABLE schedule (
                starttime VARCHAR2(6),
                endtime VARCHAR2(6),
                day VARCHAR2(10),
                matricno VARCHAR2(8),
                FOREIGN KEY(matricno) REFERENCES student(matricno) ON DELETE CASCADE,
                coursecode VARCHAR2(12),
                FOREIGN KEY(coursecode) REFERENCES subject(coursecode) ON DELETE CASCADE
            );
