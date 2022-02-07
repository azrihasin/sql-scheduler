from database import DB

class Student:
    @staticmethod
    def createTable():
        sql = """
            CREATE TABLE student (
                matricno VARCHAR2(8) NOT NULL,
                studentname VARCHAR(25) NOT NULL,
                email VARCHAR(25) NOT NULL,
                password VARCHAR(25) NOT NULL,
                kuliyyah VARCHAR(30),
                PRIMARY KEY (matricno)
            )
        """
        DB.connect()
        DB.execute(sql)
        DB.commit()
        DB.close()

    @staticmethod
    def dropTable():
        DB.connect()
        DB.execute("DROP TABLE student")
        DB.commit()
        DB.close()

    @staticmethod
    def register(matricno, studentname, email, password, kuliyyah):
        DB.connect()
        DB.execute(f"""
            INSERT INTO student VALUES
            ('{matricno}', '{studentname}', '{email}', '{password}', '{kuliyyah}')
        """)
        DB.commit()
        DB.close()
        print("register user")

    @staticmethod
    def login(email, password):
        DB.connect()
        result = DB.execute(f"SELECT * FROM student WHERE email='{email}' AND password='{password}'", type="select")
        DB.commit()
        DB.close()

        print(result)

        if len(result)>0:
            studentDetails = {
                'matricno': result[0][0],
                'studentname': result[0][1],
                'email': result[0][2],
                'password': result[0][3],
                'kuliyyah': result[0][4]
            }
            return studentDetails
        else:
            return "not found"

    @staticmethod
    def update(matricno, newmatricno, studentname, email, password, kuliyyah):
        DB.connect()
        DB.execute(f"""
            UPDATE student SET matricno='{newmatricno}', studentname='{studentname}',
            email='{email}', password='{password}', kuliyyah='{kuliyyah}'
            WHERE matricno='{matricno}'
        """)
        DB.commit()
        DB.close()

    @staticmethod
    def delete(matricno):
        DB.connect()
        DB.execute(f"DELETE FROM student WHERE matricno='{matricno}'")
        DB.commit()
        DB.close()
        print("delete ")