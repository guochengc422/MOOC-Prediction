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

if __name__ == '__main__':
    # file_truth = open("data/train/truth_train.csv").readlines()
    # file_log = open("data/train/log_train.csv").readlines()
    file_course = open("data/test/enrollment_test.csv").readlines()
    # f_out = open("data/train/log_combine_train.txt","w+")

    f_out = open("data/test/course_count.txt","w+")

    # DropDict = {}
    CourseDict = {}
    # UserDict = {}

    # for line in file_truth:
    #     infoList = line.split(',')
    #     ID = infoList[0]
    #     Truth = infoList[1]
    #     DropDict[ID] = Truth

    # for line in file_course:
    #     infoList = line.split(',')
    #     CourseDict[infoList[0]] = infoList[2]

    count = 0

    for line in file_course:

        if count%5000 == 0:
            print count

        infoList = line.split(',')
        ID = infoList[0]
        User = infoList[1]
        Course = infoList[2]

        if User in CourseDict.keys():
            CourseDict[User].append([ID,Course])

        if User not in CourseDict.keys():
            CourseDict[User] = []
            CourseDict[User].append([ID,Course])

        count+=1

    print "Course Dict Complete"
    print len(CourseDict.keys())

    for key in CourseDict.keys():
        for item in CourseDict[key]:
            ID = item[0]
            Course = item[1]
            count = str(len(CourseDict[key]))
            line = ID+','+Course
            line = line.strip()+','+count
            # print line
            f_out.write(line.strip()+'\n')

    f_out.close()
##
##
##
##
##
##
##
##
##
##

