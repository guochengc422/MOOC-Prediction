#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      GuoCheng
#
# Created:     19/06/2015
# Copyright:   (c) GuoCheng 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import fileinput

def traindatacombine():
    file_truth = open("data/train/truth_train.csv").readlines()
    file_log = open("data/train/log_train.csv").readlines()
    file_course = open("data/train/course_count.txt").readlines()
    f_out = open("data/train/log_combine_train.txt","w+")

    DropDict = {}
    CourseDict = {}
    UserDict = {}

    for line in file_truth:
        infoList = line.split(',')
        ID = infoList[0]
        Truth = infoList[1]
        DropDict[ID] = Truth

    print "DropDict Completed!"
    print len(DropDict)

    for line in file_course:
        infoList = line.split(',')
        ID = infoList[0]
        course = infoList[1]
        count = infoList[2]
        CourseDict[ID] = [course,count]

    print "CourseDict Completed!"
    print len(CourseDict)

    linecount = 0


    for line in file_log:

        # if (linecount % 5000) == 0:
        #     print linecount


        infoList = line.split(',')
        ID = infoList[0]
        Time = infoList[1]
        source = infoList[2]
        event = infoList[3]

        if source == 'server':
            source = 0
        elif source == 'browser':
            source = 1
        else:
            continue

        if event == 'problem':
            event = 0
        elif event == 'video':
            event = 1
        elif event == 'access':
            event = 2
        elif event == 'wiki':
            event = 3
        elif event == 'discussion':
            event = 4
        elif event == 'navigate':
            event = 5
        elif event == 'page_close':
            event = 6
        else:
            continue


        if UserDict.has_key(ID):
            UserDict[ID][source][event] += 1
            UserDict[ID][2].append(Time)

        elif not UserDict.has_key(ID):
            UserDict[ID] = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[]]
            UserDict[ID][source][event] += 1
            UserDict[ID][2].append(Time)

        else:
            continue

        linecount += 1


    for key in CourseDict.keys():
        if UserDict.has_key(key):
            continue
        else:
            UserDict[key] = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],['2016-01-01T10:55:13','2016-01-01T10:55:13']]

    print len(UserDict.keys())

    for key in UserDict.keys():
        if CourseDict.has_key(key):
            UserDict[key].append(CourseDict[key][0])
            UserDict[key].append(CourseDict[key][1])


        if DropDict.has_key(key):
            UserDict[key].append(DropDict[key])

    print "UserDict Complete"
    print len(UserDict.keys())


    for key in UserDict.keys():
        if len(UserDict[key]) == 6:
            outline = ''
            ID = key
            outline += ID

            for i in UserDict[key][0]:
                outline += '\t'+str(i)
            for j in UserDict[key][1]:
                outline += '\t'+str(j)

            starttime = sorted(UserDict[key][2])[0]
            endtime = sorted(UserDict[key][2])[-1]
            outline += '\t'+starttime
            outline += '\t'+endtime

            Course = UserDict[key][3]
            Count = UserDict[key][4]
            Drop = UserDict[key][5]

            outline += '\t'+Course.strip()
            outline += '\t'+Count.strip()
            outline += '\t'+Drop

            f_out.write(outline)


    f_out.close()



def CalulateTrainTime():
    file = open("data/train/log_combine_train.txt").readlines()
    f_out = open("data/train/UserID_info.txt","w+")


    monthDict = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    for line in file:
        infoList = line.split('\t')



        time1 = infoList[15]
        time2 = infoList[16]
        y1 = time1[0:4]
        m1 = time1[5:7]
        d1 = time1[8:10]

        if int(m1) == 1:
            monthday1 = 0
        else:
            monthday1 = sum([monthDict[i] for i in range(1,int(m1))])

        count1 = int(y1)*365+monthday1+int(d1)

        y2 = time2[0:4]
        m2 = time2[5:7]
        d2 = time2[8:10]

        if int(m2) == 1:
            monthday2 = 0
        else:
            monthday2 = sum([monthDict[i] for i in range(1,int(m2))])

        count2 = int(y2)*365+monthday2+int(d2)

        day = count2-count1+1

        outline = line.replace(time1+'\t'+time2,str(day))

        info= outline.split('\t')

        dropout = info[-1].strip()

        outline = ''

        outline += dropout

        for item in info[1:-1]:
            outline += '\t'+item


        f_out.write(outline+'\n')

    f_out.close()


def testdatacombine():
    file_log = open("data/test/log_test.csv").readlines()
    file_course = open("data/test/course_count.txt").readlines()
    f_out = open("data/test/log_combine_test.txt","w+")

    # DropDict = {}
    CourseDict = {}
    UserDict = {}

    # for line in file_truth:
    #     infoList = line.split(',')
    #     ID = infoList[0]
    #     Truth = infoList[1]
    #     DropDict[ID] = Truth

    # print "DropDict Completed!"
    # print len(DropDict)

    for line in file_course:
        infoList = line.split(',')
        ID = infoList[0]
        course = infoList[1]
        count = infoList[2]
        CourseDict[ID] = [course,count]

    print "CourseDict Completed!"
    print len(CourseDict)

    linecount = 0


    for line in file_log:

        if (linecount % 5000) == 0:
            print linecount


        infoList = line.split(',')
        ID = infoList[0]
        Time = infoList[1]
        source = infoList[2]
        event = infoList[3]

        if source == 'server':
            source = 0
        elif source == 'browser':
            source = 1
        else:
            continue

        if event == 'problem':
            event = 0
        elif event == 'video':
            event = 1
        elif event == 'access':
            event = 2
        elif event == 'wiki':
            event = 3
        elif event == 'discussion':
            event = 4
        elif event == 'navigate':
            event = 5
        elif event == 'page_close':
            event = 6
        else:
            continue


        if UserDict.has_key(ID):
            UserDict[ID][source][event] += 1
            UserDict[ID][2].append(Time)

        elif not UserDict.has_key(ID):
            UserDict[ID] = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[]]
            UserDict[ID][source][event] += 1
            UserDict[ID][2].append(Time)

        else:
            continue

        linecount += 1

    for key in CourseDict.keys():
        if UserDict.has_key(key):
            continue
        else:
            UserDict[key] = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],['2016-01-01T10:55:13','2016-01-01T10:55:13']]

    print len(UserDict.keys())

    for key in UserDict.keys():
        if CourseDict.has_key(key):
            UserDict[key].append(CourseDict[key][0])
            UserDict[key].append(CourseDict[key][1])


        # if DropDict.has_key(key):
        #     UserDict[key].append(DropDict[key])

    print "UserDict Complete"
    print len(UserDict.keys())


    for key in UserDict.keys():
        if len(UserDict[key]) == 5:
            outline = ''
            ID = key
            outline += ID

            for i in UserDict[key][0]:
                outline += '\t'+str(i)
            for j in UserDict[key][1]:
                outline += '\t'+str(j)

            starttime = sorted(UserDict[key][2])[0]
            endtime = sorted(UserDict[key][2])[-1]
            outline += '\t'+starttime
            outline += '\t'+endtime

            Course = UserDict[key][3]
            Count = UserDict[key][4]
            # Drop = UserDict[key][5]

            outline += '\t'+Course.strip()
            outline += '\t'+Count.strip()
            # outline += '\t'+Drop

            f_out.write(outline+'\n')


    f_out.close()



def CalulateTestTime():
    file = open("data/test/log_combine_test.txt").readlines()
    f_out = open("data/test/UserID_info.txt","w+")


    monthDict = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    for line in file:
        infoList = line.split('\t')



        time1 = infoList[15]
        time2 = infoList[16]
        y1 = time1[0:4]
        m1 = time1[5:7]
        d1 = time1[8:10]

        if int(m1) == 1:
            monthday1 = 0
        else:
            monthday1 = sum([monthDict[i] for i in range(1,int(m1))])

        count1 = int(y1)*365+monthday1+int(d1)

        y2 = time2[0:4]
        m2 = time2[5:7]
        d2 = time2[8:10]

        if int(m2) == 1:
            monthday2 = 0
        else:
            monthday2 = sum([monthDict[i] for i in range(1,int(m2))])

        count2 = int(y2)*365+monthday2+int(d2)

        day = count2-count1+1

        outline = line.replace(time1+'\t'+time2,str(day))


        f_out.write(outline)

    f_out.close()



def traindatacombineREVISED():
    file_truth = open("data/train/truth_train.csv").readlines()
    file_log = open("data/train/log_train.csv").readlines()
    file_course = open("data/train/course_count.txt").readlines()
    f_out = open("data/train/log_combine_train_revised.txt","w+")

    DropDict = {}
    CourseDict = {}
    UserDict = {}

    for line in file_truth:
        infoList = line.split(',')
        ID = infoList[0]
        Truth = infoList[1]
        DropDict[ID] = Truth

    print "DropDict Completed!"
    print len(DropDict)

    for line in file_course:
        infoList = line.split(',')
        ID = infoList[0]
        course = infoList[1]
        count = infoList[2]
        CourseDict[ID] = [course,count]

    print "CourseDict Completed!"
    print len(CourseDict)

    linecount = 0


    for line in file_log:

        if (linecount % 5000) == 0:
            print linecount


        infoList = line.split(',')
        ID = infoList[0]
        Time = infoList[1]
        source = infoList[2]
        event = infoList[3]

        monthDict = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

        year = Time[0:4]
        month = Time[5:7]
        day = Time[8:10]
        hour = int(Time[11:13])


        if int(month) == 1:
            monthday = 0
        else:
            monthday = sum([monthDict[i] for i in range(1,int(month))])

        count1 = int(year)*365+monthday+int(day)



        baselineday = 2013*365+1

        if (count1-baselineday)%7 <=5:
            weekday = (count1-baselineday)%7+2
        elif (count1-baselineday)%7 ==6:
            weekday = 1

        # print weekday



        if source == 'server':
            source = 0
        elif source == 'browser':
            source = 1
        else:
            continue

        if event == 'problem':
            event = 0
        elif event == 'video':
            event = 1
        elif event == 'access':
            event = 2
        elif event == 'wiki':
            event = 3
        elif event == 'discussion':
            event = 4
        elif event == 'navigate':
            event = 5
        elif event == 'page_close':
            event = 6
        else:
            continue


        if UserDict.has_key(ID):
            UserDict[ID][3][weekday-1] += 1
            UserDict[ID][source][event] += 1
            UserDict[ID][4][hour] += 1
            UserDict[ID][2].append(Time)

        elif not UserDict.has_key(ID):
            UserDict[ID] = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
            UserDict[ID][3][weekday-1] += 1
            UserDict[ID][source][event] += 1
            UserDict[ID][4][hour] += 1
            UserDict[ID][2].append(Time)

        else:
            continue

        linecount += 1


    for key in CourseDict.keys():
        if UserDict.has_key(key):
            continue
        else:
            UserDict[key] = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],['2016-01-01T10:55:13','2016-01-01T10:55:13'],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    print len(UserDict.keys())

    for key in UserDict.keys():
        if CourseDict.has_key(key):
            UserDict[key].append(CourseDict[key][0])
            UserDict[key].append(CourseDict[key][1])


        if DropDict.has_key(key):
            UserDict[key].append(DropDict[key])

    print "UserDict Complete"
    print len(UserDict.keys())


    for key in UserDict.keys():
        if len(UserDict[key]) == 8:
            outline = ''
            ID = key
            outline += ID

            for i in UserDict[key][0]:
                outline += '\t'+str(i)
            for j in UserDict[key][1]:
                outline += '\t'+str(j)

            starttime = sorted(UserDict[key][2])[0]
            endtime = sorted(UserDict[key][2])[-1]
            outline += '\t'+starttime
            outline += '\t'+endtime

            for i in UserDict[key][3]:
                outline += '\t'+str(i)

            for i in UserDict[key][4]:
                outline += '\t'+str(i)

            Course = UserDict[key][5]
            Count = UserDict[key][6]
            Drop = UserDict[key][7]

            outline += '\t'+Course.strip()
            outline += '\t'+Count.strip()
            outline += '\t'+Drop

            f_out.write(outline)


    f_out.close()

def CalulateTrainTimeREVISED():
    file = open("data/train/log_combine_train_revised.txt").readlines()
    f_out = open("data/train/UserID_info_revised.txt","w+")


    monthDict = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    for line in file:
        infoList = line.split('\t')



        time1 = infoList[15]
        time2 = infoList[16]
        y1 = time1[0:4]
        m1 = time1[5:7]
        d1 = time1[8:10]

        if int(m1) == 1:
            monthday1 = 0
        else:
            monthday1 = sum([monthDict[i] for i in range(1,int(m1))])

        count1 = int(y1)*365+monthday1+int(d1)

        y2 = time2[0:4]
        m2 = time2[5:7]
        d2 = time2[8:10]

        if int(m2) == 1:
            monthday2 = 0
        else:
            monthday2 = sum([monthDict[i] for i in range(1,int(m2))])

        count2 = int(y2)*365+monthday2+int(d2)

        day = count2-count1+1

        outline = line.replace(time1+'\t'+time2,str(day))

        info= outline.split('\t')

        dropout = info[-1].strip()

        outline = ''

        outline += dropout

        for item in info[1:-1]:
            outline += '\t'+item


        f_out.write(outline+'\n')

    f_out.close()


def testdatacombineREVISED():
    file_log = open("data/test/log_test.csv").readlines()
    file_course = open("data/test/course_count.txt").readlines()
    f_out = open("data/test/log_combine_test_revised.txt","w+")

    # DropDict = {}
    CourseDict = {}
    UserDict = {}

    # for line in file_truth:
    #     infoList = line.split(',')
    #     ID = infoList[0]
    #     Truth = infoList[1]
    #     DropDict[ID] = Truth

    # print "DropDict Completed!"
    # print len(DropDict)

    for line in file_course:
        infoList = line.split(',')
        ID = infoList[0]
        course = infoList[1]
        count = infoList[2]
        CourseDict[ID] = [course,count]

    print "CourseDict Completed!"
    print len(CourseDict)

    linecount = 0


    for line in file_log:

        if (linecount % 5000) == 0:
            print linecount


        infoList = line.split(',')
        ID = infoList[0]
        Time = infoList[1]
        source = infoList[2]
        event = infoList[3]

        monthDict = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

        year = Time[0:4]
        month = Time[5:7]
        day = Time[8:10]
        hour = int(Time[11:13])


        if int(month) == 1:
            monthday = 0
        else:
            monthday = sum([monthDict[i] for i in range(1,int(month))])

        count1 = int(year)*365+monthday+int(day)



        baselineday = 2013*365+1

        if (count1-baselineday)%7 <=5:
            weekday = (count1-baselineday)%7+2
        elif (count1-baselineday)%7 ==6:
            weekday = 1

        # print weekday



        if source == 'server':
            source = 0
        elif source == 'browser':
            source = 1
        else:
            continue

        if event == 'problem':
            event = 0
        elif event == 'video':
            event = 1
        elif event == 'access':
            event = 2
        elif event == 'wiki':
            event = 3
        elif event == 'discussion':
            event = 4
        elif event == 'navigate':
            event = 5
        elif event == 'page_close':
            event = 6
        else:
            continue


        if UserDict.has_key(ID):
            UserDict[ID][3][weekday-1] += 1
            UserDict[ID][source][event] += 1
            UserDict[ID][4][hour] += 1
            UserDict[ID][2].append(Time)

        elif not UserDict.has_key(ID):
            UserDict[ID] = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
            UserDict[ID][3][weekday-1] += 1
            UserDict[ID][source][event] += 1
            UserDict[ID][4][hour] += 1
            UserDict[ID][2].append(Time)

        else:
            continue

        linecount += 1


    for key in CourseDict.keys():
        if UserDict.has_key(key):
            continue
        else:
            UserDict[key] = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],['2016-01-01T10:55:13','2016-01-01T10:55:13'],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    print len(UserDict.keys())

    for key in UserDict.keys():
        if CourseDict.has_key(key):
            UserDict[key].append(CourseDict[key][0])
            UserDict[key].append(CourseDict[key][1])


        # if DropDict.has_key(key):
        #     UserDict[key].append(DropDict[key])

    print "UserDict Complete"
    print len(UserDict.keys())


    for key in UserDict.keys():
        if len(UserDict[key]) == 7:
            outline = ''
            ID = key
            outline += ID

            for i in UserDict[key][0]:
                outline += '\t'+str(i)
            for j in UserDict[key][1]:
                outline += '\t'+str(j)

            starttime = sorted(UserDict[key][2])[0]
            endtime = sorted(UserDict[key][2])[-1]
            outline += '\t'+starttime
            outline += '\t'+endtime

            for i in UserDict[key][3]:
                outline += '\t'+str(i)

            for i in UserDict[key][4]:
                outline += '\t'+str(i)

            Course = UserDict[key][5]
            Count = UserDict[key][6]
            # Drop = UserDict[key][7]

            outline += '\t'+Course.strip()
            outline += '\t'+Count
            # outline += '\t'+Drop

            f_out.write(outline)


    f_out.close()


def CalulateTestTimeREVISED():
    file = open("data/test/log_combine_test_revised.txt").readlines()
    f_out = open("data/test/UserID_info_revised.txt","w+")


    monthDict = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    for line in file:
        infoList = line.split('\t')



        time1 = infoList[15]
        time2 = infoList[16]
        y1 = time1[0:4]
        m1 = time1[5:7]
        d1 = time1[8:10]

        if int(m1) == 1:
            monthday1 = 0
        else:
            monthday1 = sum([monthDict[i] for i in range(1,int(m1))])

        count1 = int(y1)*365+monthday1+int(d1)

        y2 = time2[0:4]
        m2 = time2[5:7]
        d2 = time2[8:10]

        if int(m2) == 1:
            monthday2 = 0
        else:
            monthday2 = sum([monthDict[i] for i in range(1,int(m2))])

        count2 = int(y2)*365+monthday2+int(d2)

        day = count2-count1+1

        outline = line.replace(time1+'\t'+time2,str(day))


        f_out.write(outline)

    f_out.close()




# traindatacombine()
# CalulateTrainTime()
# testdatacombine()
# CalulateTestTime()

# traindatacombineREVISED()
# CalulateTrainTimeREVISED()
# testdatacombineREVISED()
CalulateTestTimeREVISED()