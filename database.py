import cx_Oracle

class DB:
    connection = None
    cursor = None

    @classmethod
    def connect(cls):
        cls.connection = cx_Oracle.connect("system", "db", "localhost/xe")
        cls.cursor = cls.connection.cursor()

    @classmethod
    def execute(cls, sql, type="not select"):
        cls.cursor.execute(sql)
        if type == "select":
            result = []
            for row in cls.cursor:
                result.append(row)
            return result
        else:
            return "done"
            
    @classmethod
    def commit(cls):
        cls.cursor.execute("commit")

    @classmethod
    def close(cls):
        cls.cursor.close()
        cls.connection.close()

def test():
    DB.connect()
    result = DB.execute("select * from testtable where name='didi'", type="select")
    DB.commit()
    DB.close()
    print(result)