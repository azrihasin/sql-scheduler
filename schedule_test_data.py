"""

def insertScheduleTestData():
    for s in scheduleTestData:
        Schedule.addsubject(
            s['matricno'], s['day'], s['subject'],
            s['starttime'], s['endtime']
        )

scheduleTestData = [
    { #1
        'matricno': studentTestData[0]['matricno'],
        'day': 'monday',
        'subject': subjectList[0],
        'starttime': '0900',
        'endtime': '1050'
    },
    { #2
        'matricno': studentTestData[0]['matricno'],
        'day': 'monday',
        'subject': subjectList[1],
        'starttime': '1100',
        'endtime': '1245'
    },
    { #3
        'matricno': studentTestData[0]['matricno'],
        'day': 'monday',
        'subject': subjectList[2],
        'starttime': '1400',
        'endtime': '1520'
    },
    { #4
        'matricno': studentTestData[0]['matricno'],
        'day': 'tuesday',
        'subject': subjectList[8],
        'starttime': '1000',
        'endtime': '1200'
    },
    { #5
        'matricno': studentTestData[0]['matricno'],
        'day': 'tuesday',
        'subject': subjectList[7],
        'starttime': '1430',
        'endtime': '1600'
    },
    { #6
        'matricno': studentTestData[0]['matricno'],
        'day': 'wednesday',
        'subject': subjectList[0],
        'starttime': '0900',
        'endtime': '1050'
    },
    { #7
        'matricno': studentTestData[0]['matricno'],
        'day': 'wednesday',
        'subject': subjectList[1],
        'starttime': '1100',
        'endtime': '1245'
    },
    { #8
        'matricno': studentTestData[0]['matricno'],
        'day': 'wednesday',
        'subject': subjectList[2],
        'starttime': '1400',
        'endtime': '1520'
    },
    { #9
        'matricno': studentTestData[0]['matricno'],
        'day': 'thursday',
        'subject': subjectList[8],
        'starttime': '1000',
        'endtime': '1200'
    },
    { #10
        'matricno': studentTestData[0]['matricno'],
        'day': 'thursday',
        'subject': subjectList[7],
        'starttime': '1430',
        'endtime': '1600'
    },
    { #11
        'matricno': studentTestData[0]['matricno'],
        'day': 'friday',
        'subject': subjectList[11],
        'starttime': '1030',
        'endtime': '1230'
    },
    #student 2
    { #1
        'matricno': studentTestData[1]['matricno'],
        'day': 'monday',
        'subject': subjectList[4],
        'starttime': '0840',
        'endtime': '1030'
    },
    { #2
        'matricno': studentTestData[1]['matricno'],
        'day': 'monday',
        'subject': subjectList[1],
        'starttime': '1100',
        'endtime': '1245'
    },
    { #3
        'matricno': studentTestData[1]['matricno'],
        'day': 'monday',
        'subject': subjectList[2],
        'starttime': '1400',
        'endtime': '1520'
    },
    { #4
        'matricno': studentTestData[1]['matricno'],
        'day': 'tuesday',
        'subject': subjectList[3],
        'starttime': '1000',
        'endtime': '1200'
    },
    { #5
        'matricno': studentTestData[1]['matricno'],
        'day': 'tuesday',
        'subject': subjectList[0],
        'starttime': '1430',
        'endtime': '1600'
    },
    { #6
        'matricno': studentTestData[1]['matricno'],
        'day': 'wednesday',
        'subject': subjectList[4],
        'starttime': '0900',
        'endtime': '1050'
    },
    { #7
        'matricno': studentTestData[1]['matricno'],
        'day': 'wednesday',
        'subject': subjectList[1],
        'starttime': '1100',
        'endtime': '1245'
    },
    { #8
        'matricno': studentTestData[1]['matricno'],
        'day': 'wednesday',
        'subject': subjectList[2],
        'starttime': '1400',
        'endtime': '1520'
    },
    { #9
        'matricno': studentTestData[1]['matricno'],
        'day': 'thursday',
        'subject': subjectList[3],
        'starttime': '1000',
        'endtime': '1200'
    },
    { #10
        'matricno': studentTestData[1]['matricno'],
        'day': 'thursday',
        'subject': subjectList[0],
        'starttime': '1430',
        'endtime': '1600'
    },
    { #11
        'matricno': studentTestData[1]['matricno'],
        'day': 'thursday',
        'subject': subjectList[9],
        'starttime': '1700',
        'endtime': '1850'
    },
    { #12
        'matricno': studentTestData[1]['matricno'],
        'day': 'friday',
        'subject': subjectList[11],
        'starttime': '1030',
        'endtime': '1230'
    },
    #student 3
    { #1
        'matricno': studentTestData[2]['matricno'],
        'day': 'monday',
        'subject': subjectList[4],
        'starttime': '1100',
        'endtime': '1245'
    },
    { #2
        'matricno': studentTestData[2]['matricno'],
        'day': 'monday',
        'subject': subjectList[3],
        'starttime': '1430',
        'endtime': '1550'
    },
    { #3
        'matricno': studentTestData[2]['matricno'],
        'day': 'monday',
        'subject': subjectList[7],
        'starttime': '1650',
        'endtime': '1800'
    },
    { #4
        'matricno': studentTestData[2]['matricno'],
        'day': 'tuesday',
        'subject': subjectList[8],
        'starttime': '1000',
        'endtime': '1200'
    },
    { #5
        'matricno': studentTestData[2]['matricno'],
        'day': 'tuesday',
        'subject': subjectList[6],
        'starttime': '1530',
        'endtime': '1700'
    },
    { #6
        'matricno': studentTestData[2]['matricno'],
        'day': 'wednesday',
        'subject': subjectList[4],
        'starttime': '1100',
        'endtime': '1245'
    },
    { #7
        'matricno': studentTestData[2]['matricno'],
        'day': 'wednesday',
        'subject': subjectList[3],
        'starttime': '1430',
        'endtime': '1550'
    },
    { #8
        'matricno': studentTestData[2]['matricno'],
        'day': 'wednesday',
        'subject': subjectList[7],
        'starttime': '1650',
        'endtime': '1800'
    },
    { #9
        'matricno': studentTestData[2]['matricno'],
        'day': 'thursday',
        'subject': subjectList[8],
        'starttime': '1000',
        'endtime': '1200'
    },
    { #10
        'matricno': studentTestData[2]['matricno'],
        'day': 'thursday',
        'subject': subjectList[6],
        'starttime': '1430',
        'endtime': '1600'
    },
    { #11
        'matricno': studentTestData[2]['matricno'],
        'day': 'friday',
        'subject': subjectList[11],
        'starttime': '1400',
        'endtime': '1600'
    },
    #student 4
    { #1
        'matricno': studentTestData[3]['matricno'],
        'day': 'monday',
        'subject': subjectList[0],
        'starttime': '1000',
        'endtime': '1130'
    },
    { #2
        'matricno': studentTestData[3]['matricno'],
        'day': 'monday',
        'subject': subjectList[5],
        'starttime': '1400',
        'endtime': '1540'
    },
    { #3
        'matricno': studentTestData[3]['matricno'],
        'day': 'tuesday',
        'subject': subjectList[7],
        'starttime': '1045',
        'endtime': '1200'
    },
    { #4
        'matricno': studentTestData[3]['matricno'],
        'day': 'tuesday',
        'subject': subjectList[8],
        'starttime': '1400',
        'endtime': '1530'
    },
    { #5
        'matricno': studentTestData[3]['matricno'],
        'day': 'tuesday',
        'subject': subjectList[9],
        'starttime': '1550',
        'endtime': '1700'
    },
    { #6
        'matricno': studentTestData[3]['matricno'],
        'day': 'wednesday',
        'subject': subjectList[0],
        'starttime': '1000',
        'endtime': '1130'
    },
    { #7
        'matricno': studentTestData[3]['matricno'],
        'day': 'wednesday',
        'subject': subjectList[5],
        'starttime': '1400',
        'endtime': '1540'
    },
    { #8
        'matricno': studentTestData[3]['matricno'],
        'day': 'thursday',
        'subject': subjectList[7],
        'starttime': '1400',
        'endtime': '1520'
    },
    { #9
        'matricno': studentTestData[3]['matricno'],
        'day': 'thursday',
        'subject': subjectList[8],
        'starttime': '1700',
        'endtime': '1850'
    },
    { #10
        'matricno': studentTestData[3]['matricno'],
        'day': 'friday',
        'subject': subjectList[9],
        'starttime': '0900',
        'endtime': '1030'
    },
    { #11
        'matricno': studentTestData[3]['matricno'],
        'day': 'friday',
        'subject': subjectList[11],
        'starttime': '1030',
        'endtime': '1230'
    },
    { #12
        'matricno': studentTestData[3]['matricno'],
        'day': 'sunday',
        'subject': subjectList[3],
        'starttime': '1000',
        'endtime': '1200'
    },
    #student 5
    { #1
        'matricno': studentTestData[4]['matricno'],
        'day': 'monday',
        'subject': subjectList[6],
        'starttime': '0830',
        'endtime': '1030'
    },
    { #2
        'matricno': studentTestData[4]['matricno'],
        'day': 'monday',
        'subject': subjectList[5],
        'starttime': '1050',
        'endtime': '1215'
    },
    { #3
        'matricno': studentTestData[4]['matricno'],
        'day': 'monday',
        'subject': subjectList[4],
        'starttime': '1400',
        'endtime': '1520'
    },
    { #4
        'matricno': studentTestData[4]['matricno'],
        'day': 'monday',
        'subject': subjectList[3],
        'starttime': '1530',
        'endtime': '1650'
    },
    { #5
        'matricno': studentTestData[4]['matricno'],
        'day': 'tuesday',
        'subject': subjectList[7],
        'starttime': '1430',
        'endtime': '1600'
    },
    { #6
        'matricno': studentTestData[4]['matricno'],
        'day': 'tuesday',
        'subject': subjectList[0],
        'starttime': '1610',
        'endtime': '1800'
    },
    { #7
        'matricno': studentTestData[4]['matricno'],
        'day': 'wednesday',
        'subject': subjectList[6],
        'starttime': '0830',
        'endtime': '1030'
    },
    { #8
        'matricno': studentTestData[4]['matricno'],
        'day': 'wednesday',
        'subject': subjectList[5],
        'starttime': '1050',
        'endtime': '1215'
    },
    { #9
        'matricno': studentTestData[4]['matricno'],
        'day': 'wednesday',
        'subject': subjectList[4],
        'starttime': '1400',
        'endtime': '1520'
    },
    { #10
        'matricno': studentTestData[4]['matricno'],
        'day': 'wednesday',
        'subject': subjectList[3],
        'starttime': '1530',
        'endtime': '1650'
    },
    { #11
        'matricno': studentTestData[4]['matricno'],
        'day': 'thursday',
        'subject': subjectList[7],
        'starttime': '1430',
        'endtime': '1600'
    },
    { #12
        'matricno': studentTestData[4]['matricno'],
        'day': 'thursday',
        'subject': subjectList[0],
        'starttime': '1610',
        'endtime': '1800'
    },
    { #13
        'matricno': studentTestData[4]['matricno'],
        'day': 'friday',
        'subject': subjectList[11],
        'starttime': '1030',
        'endtime': '1230'
    },
    { #14
        'matricno': studentTestData[4]['matricno'],
        'day': 'saturday',
        'subject': subjectList[3],
        'starttime': '1030',
        'endtime': '1230'
    }
]"""