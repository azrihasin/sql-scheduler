from database import DB

class Schedule:
    @staticmethod
    def createTable():
        sql = """
            CREATE TABLE schedule (
                matricno VARCHAR(10) NOT NULL,
                day VARCHAR2(10) NOT NULL,
                subject VARCHAR(20) NOT NULL,
                starttime VARCHAR(8) NOT NULL,
                endtime VARCHAR(8) NOT NULL
            )
        """
        DB.connect()
        DB.execute(sql)
        DB.commit()
        DB.close()

    @staticmethod
    def dropTable():
        DB.connect()
        DB.execute("DROP TABLE schedule")
        DB.commit()
        DB.close()

    @staticmethod
    def addsubject(matricno, day, subject, starttime, endtime):
        DB.connect()
        DB.execute(f"""
            INSERT INTO schedule VALUES
            ('{matricno}', '{day}', '{subject}', '{starttime}', '{endtime}')
        """)
        DB.commit()
        DB.close()
        print("add subject")

    @staticmethod
    def getschedule(matricno):
        DB.connect()
        result = DB.execute(f"SELECT * FROM schedule WHERE matricno='{matricno}'", type="select")
        DB.commit()
        DB.close()

        print(result)

        if len(result)>0:
            schedule = []
            for detail in result:
                schedule.append({
                    'day': detail[1],
                    'subject': detail[2],
                    'starttime': detail[3],
                    'endtime': detail[4]
                })
            return schedule
        else:
            return "not found"

    @staticmethod
    def update(matricno, day, oldsubject, newsubject, oldstarttime, newstarttime, endtime):
        DB.connect()
        DB.execute(f"""
            UPDATE schedule SET
            subject='{newsubject}', starttime='{newstarttime}', endtime='{endtime}'
            WHERE matricno='{matricno}' AND day='{day}' AND subject='{oldsubject}'
            AND starttime='{oldstarttime}'
        """)
        DB.commit()
        DB.close()

    @staticmethod
    def delete(matricno, day, subject, starttime):
        DB.connect()
        DB.execute(f"""
            DELETE FROM schedule WHERE matricno='{matricno}' 
            AND day='{day}' AND subject='{subject}' AND starttime='{starttime}'
        """)
        DB.commit()
        DB.close()
        print("delete schedule")