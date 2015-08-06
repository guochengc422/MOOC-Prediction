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
    # file_course = open("data/train/UserID_info.txt").readlines()
    # file_course = open("data/test/UserID_info.txt").readlines()

    # f_out = open("data/train/UserInfo_final.txt","w+")
    # f_out = open("data/test/UserInfo_final.txt","w+")

    # file_course = open("data/train/UserID_info_revised.txt").readlines()
    file_course = open("data/test/UserID_info_revised.txt").readlines()

    # f_out = open("data/train/UserInfo_final_revised.txt","w+")
    f_out = open("data/test/UserInfo_final_revised.txt","w+")


    courseDict = {}

    count = 0

    for line in file_course:

        infoList = line.strip('\n').split('\t')

        course = infoList[-2]

        if courseDict.has_key(course):
            continue
        elif not courseDict.has_key(course):
            courseDict[course] = count
            count += 1

    print len(courseDict.keys())


    for line in file_course:

        info = line.strip('\n').split()

        course = info[-2]

        outline = line.replace(course,str(courseDict[course]))

        f_out.write(outline)

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

