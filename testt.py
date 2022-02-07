from database import DB

DB.connect()
DB.execute("""
INSERT INTO student VALUES
            ('1812129', 'ahmad', 'ahmad@gmail.com',
            '1234', 'kict');
""")
DB.commit()
DB.close()