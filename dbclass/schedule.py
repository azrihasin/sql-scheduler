from database import DB

class Schedule:
    @staticmethod
    def addsubject(starttime, endtime, day, matricno, coursecode):
        DB.connect()
        DB.execute(f"""
            INSERT INTO schedule VALUES
            ('{starttime}', '{endtime}', '{day}', '{matricno}', '{coursecode}')
        """)
        DB.commit()
        DB.close()
        print("add subject")

    @staticmethod
    def getschedule(matricno):
        returndata = []
        index = 0
        DB.connect()
        result = DB.execute(f"SELECT * FROM schedule WHERE matricno='{matricno}'", type="select")
        if len(result) > 0:
            for row in result:
                subjdetails = DB.execute(f"SELECT subjectname, credithour, placeid FROM subject WHERE coursecode='{row[4]}'", type="select")
                #print(subjdetails)
                placedetails = DB.execute(f"SELECT placename, placelevel, placeblock FROM place WHERE placeid='{subjdetails[0][2]}'", type="select")
                #print(placedetails)
                returndata.append({
                    'starttime': row[0],
                    'endtime': row[1],
                    'day': row[2],
                    'coursecode': row[4],
                    'subjectname': subjdetails[0][0],
                    'credithour': subjdetails[0][1],
                    'placename': placedetails[0][0],
                    'placelevel': placedetails[0][1],
                    'placeblock': placedetails[0][2]
                })
            DB.commit()
            DB.close()
            print(result)
            return returndata
        else:
            return "not found"   
                        
        

            

    @staticmethod
    def update(matricno, day, oldcoursecode, newcoursecode, oldstarttime, newstarttime, endtime):
        DB.connect()
        DB.execute(f"""
            UPDATE schedule SET
            coursecode='{newcoursecode}', starttime='{newstarttime}', endtime='{endtime}'
            WHERE matricno='{matricno}' AND day='{day}' AND coursecode='{oldcoursecode}'
            AND starttime='{oldstarttime}'
        """)
        DB.commit()
        DB.close()

    @staticmethod
    def delete(matricno, day, coursecode, starttime):
        DB.connect()
        DB.execute(f"""
            DELETE FROM schedule WHERE matricno='{matricno}' 
            AND day='{day}' AND coursecode='{coursecode}' AND starttime='{starttime}'
        """)
        DB.commit()
        DB.close()
        print("delete schedule")

if __name__ == "__main__":
    print(Schedule.getschedule('1812129'))