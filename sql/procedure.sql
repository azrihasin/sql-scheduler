CREATE OR REPLACE PROCEDURE getstudentdetails
(matric student.matricno%TYPE)
IS
s_name VARCHAR2(20),
s_matricno VARCHAR2(10),
s_email VARCHAR2(20),
s_kuliyyah VARCHAR2(20)
BEGIN
SELECT studentname, matricno, email, kuliyyah INTO s_name, s_matricno, s_email, s_kuliyyah
FROM student
WHERE matricno = &matricno;
DBMS_OUTPUT.put_line('Student details: ' || s_name || s_matricno || s_email || s_kuliyyah);
END getstudentdetails;

CREATE OR REPLACE PROCEDURE getsubjectname
(f_name patient.pt_fname%TYPE,
l_name patient.pt_lname%TYPE,
birth_date patient.ptdob%TYPE,
original_date IN OUT DATE,
new_date IN DATE)
AS
BEGIN
SELECT nextapptdate INTO original_date
FROM patient
WHERE pt_fname = f_name AND pt_lname = l_name AND ptdob = birth_date;
UPDATE patient
SET nextapptdate = new_date
WHERE pt_fname = f_name AND pt_lname = l_name AND ptdob = birth_date;
DBMS_OUTPUT.put_line('The data has been updated.');
DBMS_OUTPUT.put_line('The original next appointmentdate was ' || original_date);
END getsubjectname;