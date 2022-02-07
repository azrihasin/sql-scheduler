from user import Student
from table import Schedule

subjectList = [
    'csc 1100', 'csc 5000', 'info 2200', 'info 9900', 'info 2401', 'le 4000',
    'ungs 2000', 'ungs 5600', 'titas 1200', 'ke 4000', 'ki 1120', 'ccub 2000'
]

studentTestData = [
    {
        'matricno': '1812129',
        'studentname': 'ahmad',
        'email': 'ahmad@gmail.com',
        'password': '1234',
        'kulliyyah': 'kict'
    },
    {
        'matricno': '1234567',
        'studentname': 'ali',
        'email': 'ali@gmail.com',
        'password': '2345',
        'kulliyyah': 'kaed'
    },
    {
        'matricno': '1712234',
        'studentname': 'rosli',
        'email': 'rosli@gmail.com',
        'password': '3456',
        'kulliyyah': 'kict'
    },
    {
        'matricno': '1621111',
        'studentname': 'sarah',
        'email': 'sarah@email.com',
        'password': '4567',
        'kulliyyah': 'koe'
    },
    {
        'matricno': '1726678',
        'studentname': 'yusri',
        'email': 'yusri@gmail.com',
        'password': '7788',
        'kulliyyah': 'kemns'
    },
    {
        'matricno': '1812130',
        'studentname': 'eddie',
        'email': 'eddie@gmail.com',
        'password': '1234',
        'kulliyyah': 'kict'
    },
    {
        'matricno': '1812131',
        'studentname': 'hazim',
        'email': 'hazim@gmail.com',
        'password': '7899',
        'kulliyyah': 'kaed'
    },
    {
        'matricno': '1812132',
        'studentname': 'rizal',
        'email': 'rizal@gmail.com',
        'password': '3456',
        'kulliyyah': 'koe'
    },
    {
        'matricno': '1812133',
        'studentname': 'omar',
        'email': 'omar@email.com',
        'password': '4567',
        'kulliyyah': 'koe'
    },
    {
        'matricno': '1812134',
        'studentname': 'hanis',
        'email': 'hanis@gmail.com',
        'password': '7788',
        'kulliyyah': 'kemns'
    }
]

placeTestData = [
    {
        'placeid': '1',
        'placename': 'lab 2',
        'placelevel': 1,
        'placeblock': 'c'
    },
    {
        'placeid': '2',
        'placename': 'lab 3',
        'placelevel': 1,
        'placeblock': 'd'
    },
    {
        'placeid': '3',
        'placename': 'lab 5',
        'placelevel': 3,
        'placeblock': 'e'
    }
]

subjectTestData = [
    {
        'coursecode': 'CSC 1100',
        'subjectname': 'element of programming',
        'credithour': 3,
        'placeid': '2'
    },
    {
        'coursecode': 'CSC 1200',
        'subjectname': 'oop',
        'credithour': 3,
        'placeid': '1'
    },
    {
        'coursecode': 'UNGS 1100',
        'subjectname': 'ungs',
        'credithour': 2,
        'placeid': '3'
    }
]

scheduleTestData = [
    { #1
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[0]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #2
        'starttime': '1100',
        'endtime': '1250',
        'day': 'monday',
        'matricno': studentTestData[0]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #3
        'starttime': '1400',
        'endtime': '1530',
        'day': 'monday',
        'matricno': studentTestData[0]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #4
        'starttime': '1530',
        'endtime': '1620',
        'day': 'monday',
        'matricno': studentTestData[0]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #5
        'starttime': '0900',
        'endtime': '1020',
        'day': 'tuesday',
        'matricno': studentTestData[0]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #6
        'starttime': '1030',
        'endtime': '1230',
        'day': 'tuesday',
        'matricno': studentTestData[0]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #7
        'starttime': '1400',
        'endtime': '1520',
        'day': 'wednesday',
        'matricno': studentTestData[0]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #8
        'starttime': '1530',
        'endtime': '1250',
        'day': 'wednesday',
        'matricno': studentTestData[0]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #9
        'starttime': '1000',
        'endtime': '1120',
        'day': 'thursday',
        'matricno': studentTestData[0]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #10
        'starttime': '1130',
        'endtime': '1250',
        'day': 'thursday',
        'matricno': studentTestData[0]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #11
        'starttime': '1030',
        'endtime': '1230',
        'day': 'friday',
        'matricno': studentTestData[0]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    #student 2
    { #1
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[1]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #2
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[1]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #3
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[1]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #4
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[1]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #5
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[1]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #6
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[1]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #7
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[1]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #8
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[1]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #9
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[1]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #10
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[1]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #11
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[1]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    #student 3
    { #1
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[2]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #2
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[2]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #3
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[2]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #4
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[2]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #5
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[2]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #6
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[2]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #7
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[2]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #8
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[2]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #9
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[2]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #10
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[2]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #11
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[2]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    # student 4
    { #1
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[3]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #2
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[3]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #3
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[3]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #4
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[3]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #5
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[3]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #6
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[3]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #7
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[3]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #8
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[3]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #9
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[3]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #10
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[3]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #11
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[3]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    # student 5
    { #1
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[4]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #2
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[4]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #3
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[4]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #4
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[4]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #5
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[4]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #6
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[4]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #7
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[4]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #8
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[4]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #9
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[4]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #10
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[4]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #11
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[4]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    # student6
    { #1
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[5]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #2
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[5]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #3
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[5]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #4
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[5]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #5
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[5]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #6
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[5]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #7
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[5]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #8
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[5]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #9
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[5]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #10
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[5]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #11
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[5]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    # student 7
    { #1
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[6]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #2
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[6]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #3
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[6]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #4
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[6]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #5
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[6]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #6
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[6]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #7
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[6]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #8
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[6]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #9
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[6]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #10
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[6]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #11
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[6]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    #student 8
    { #1
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[7]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #2
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[7]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #3
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[7]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #4
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[7]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #5
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[7]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #6
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[7]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #7
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[7]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #8
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[7]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #9
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[7]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #10
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[7]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #11
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[7]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    #student 9
    { #1
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[8]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #2
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[8]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #3
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[8]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #4
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[8]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #5
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[8]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #6
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[8]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #7
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[8]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #8
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[8]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #9
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[8]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #10
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[8]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #11
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[8]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    # student 10
    { #1
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[9]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #2
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[9]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #3
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[9]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #4
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[9]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #5
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[9]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #6
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[9]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #7
        'starttime': '0830',
        'endtime': '1000',
        'day': 'monday',
        'matricno': studentTestData[9]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #8
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[9]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #9
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[9]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #10
        'starttime': '1100',
        'endtime': '1250',
        'day': 'tuesday',
        'matricno': studentTestData[9]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
    { #11
        'starttime': '1400',
        'endtime': '1530',
        'day': 'wednesday',
        'matricno': studentTestData[9]['matricno'],
        'coursecode': subjectTestData[0]['coursecode'],
    },
]

def insertStudentTestData():
    for student in studentTestData:
        Student.register(
            student['matricno'], student['studentname'], 
            student['email'], student['password'], student['kulliyyah']
        )

def insertPlaceTestData():
    for place in placeTestData:
        pass

def insertSubjectTestData():
    pass

def insertScheduleTestData():
    pass

def resetDatabase():
    Student.dropTable()
    Schedule.dropTable()

def initializeDatabase():
    Student.createTable()
    insertStudentTestData()
    Schedule.createTable()
    insertScheduleTestData()

def generateInsertCommand():
    file = open('sql/timetable_data.sql', 'w')
    s = ''
    for student in studentTestData:
        s += f"""
            INSERT INTO student VALUES
            ('{student['matricno']}', '{student['studentname']}', '{student['email']}',
            '{student['password']}', '{student['kulliyyah']}');
        """

    s += "\n\n\n"

    for place in placeTestData:
        s += f"""
            INSERT INTO place VALUES
            ('{place['placeid']}', '{place['placename']}', {place['placelevel']},
            '{place['placeblock']}');
        """

    s += "\n\n\n"

    for subject in subjectTestData:
        s += f"""
            INSERT INTO subject VALUES
            ('{subject['coursecode']}', '{subject['subjectname']}', {subject['credithour']},
            '{subject['placeid']}');
        """

    s += "\n\n\n"

    for schedule in scheduleTestData:
        s += f"""
            INSERT INTO schedule VALUES
            ('{schedule['starttime']}', '{schedule['endtime']}', '{schedule['day']}',
            '{schedule['matricno']}', '{schedule['coursecode']}');
        """
    file.write(s)
    file.close()

if __name__ == '__main__':
    generateInsertCommand()