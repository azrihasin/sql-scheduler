CREATE OR REPLACE PROCEDURE getstudentdetails
(matric IN VARCHAR2)
IS
s_name VARCHAR2(20),
s_matricno VARCHAR2(10):=&matric,
s_email VARCHAR2(20),
s_kuliyyah VARCHAR2(20)
BEGIN
SELECT studentname, matricno, email, kuliyyah INTO s_name, s_matricno, s_email, s_kuliyyah
FROM student
WHERE matricno = s_matricno;
DBMS_OUTPUT.put_line('Student details: ' || s_name || s_matricno || s_email || s_kuliyyah);
END getstudentdetails;
/

ACCEPT s_matricno PROMPT 'Enter student matric no: '
BEGIN
modifydate ('&s_matricno')
END;
/