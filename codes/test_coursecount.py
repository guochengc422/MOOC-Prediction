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
    file_course = open("data/train/UserInfo_final.txt").readlines()
    # file_course = open("data/test/UserInfo_final.txt").readlines()

    # f_out = open("data/train/train.csv","w+")
    # f_out = open("data/test/test.csv","w+")
    # f_out.write('dropout,s_positive,s_negative,s_navigate,s_close,b_positive,b_negative,b_navigate,b_close,day,courseID,coursecount'+'\n')
    # f_out.write('UserID,s_positive,s_negative,s_navigate,s_close,b_positive,b_negative,b_navigate,b_close,day,courseID,coursecount'+'\n')
    
    count1 = 0

    count2 = 0

    for line in file_course:

            infoList = line.split('\t')

            dropout = infoList[0]
            coursecount = int(infoList[-1])
            s_positive = int(infoList[1])
            courseID = int(infoList[-2])

            day = int(infoList[-3])

            if(courseID==5 and dropout=='1'):
                count1+=1

            if(courseID==5):
                count2+=1

    print count1

    print count2


