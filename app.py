from flask import Flask, render_template, jsonify, request
import cx_Oracle
# import sys
# sys.path.insert(1, 'C:/Users/User/Documents/database/project/dbclass')
from dbclass.student import Student
from dbclass.schedule import Schedule
from dbclass.database import DB
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    DB.connect()
    result = DB.execute("SELECT * FROM student WHERE email='ahmad@gmail.com' AND password='1234'", type="select")
    DB.commit()
    DB.close()
    print(result)
    return jsonify(result)


#####################
# start user routes #
#####################
@app.route('/user/register', methods=['POST', 'GET'])
def register():
    data = request.json
    Student.register(data['matricno'], data['studentname'], data['email'], data['password'], data['kulliyyah'])
    studentinfo = Student.login(data['email'], data['password'])
    return jsonify(studentinfo)

@app.route('/user/login', methods=['POST', 'GET'])
def userlogin():
    data = request.json
    studentinfo = Student.login(data['email'], data['password'])
    if studentinfo == "not found":
        return jsonify(["not found"])
    else:
        schedule = Schedule.getschedule(studentinfo['matricno'])
        return jsonify({
            'schedule': schedule,
            'studentinfo': studentinfo
        })

@app.route('/user/update', methods=['POST', 'GET'])
def updateuser():
    data = request.json
    print(data)
    Student.update(
        data['matricno'], data['newmatricno'],
        data['studentname'], data['email'], data['password'], data['kulliyyah']
    )
    return jsonify(['updated'])

@app.route('/user/delete', methods=['POST', 'GET'])
def deleteuser():
    data = request.json
    Student.delete(data['matricno'])
    return jsonify(["student deleted"])

###################
# end user routes #
###################

######################
# start table routes #
######################

@app.route('/table/add', methods=['POST', 'GET'])
def addsubject():
    data = request.json
    Schedule.addsubject(
        data['starttime'], data['endtime'],
        data['day'], data['matricno'], data['coursecode']
    )
    return jsonify(["subject added"])

@app.route('/table/update', methods=['POST', 'GET'])
def updatescedule():
    data = request.json
    Schedule.update(
        data['matricno'], data['day'], data['oldsubject'], data['newsubject'],
        data['oldstarttime'], data['newstarttime'], data['endtime']
    )
    return jsonify(["schedule updated"])

@app.route('/table/delete', methods=['POST', 'GET'])
def deleteSubject():
    data = request.json
    Schedule.delete(data['matricno'], data['day'], data['subject'], data['starttime'])
    return jsonify(["subject deleted"])

####################
# end table routes #
####################

if __name__ == '__main__':
    app.run(debug=True)