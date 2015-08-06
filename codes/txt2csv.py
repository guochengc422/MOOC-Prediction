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
    # file_course = open("data/train/UserInfo_final.txt").readlines()
    # file_course = open("data/test/UserInfo_final.txt").readlines()

    # f_out = open("data/train/train.csv","w+")
    # f_out = open("data/test/test.csv","w+")

    # file_course = open("data/train/UserInfo_final_revised.txt").readlines()
    file_course = open("data/test/UserInfo_final_revised.txt").readlines()

    # f_out = open("data/train/train.csv","w+")
    f_out = open("data/test/test.csv","w+")


    # f_out.write('dropout,s1,s2,s3,s4,s5,s6,s7,b1,b2,b3,b4,b5,b6,b7,day,courseID,coursecount'+'\n')
    # f_out.write('UserID,s1,s2,s3,s4,s5,s6,s7,b1,b2,b3,b4,b5,b6,b7,day,courseID,coursecount'+'\n')


    # f_out.write('dropout,s_positive,s_negative,s_navigate,s_close,b_positive,b_negative,b_navigate,b_close,day,courseID,coursecount'+'\n')
    # f_out.write('UserID,s_positive,s_negative,s_navigate,s_close,b_positive,b_negative,b_navigate,b_close,day,courseID,coursecount'+'\n')


    # f_out.write('dropout,s1,s2,s3,s4,s5,s6,s7,b1,b2,b3,b4,b5,b6,b7,day,w1,w2,w3,w4,w5,w6,w7,courseID,coursecount'+'\n')
    # f_out.write('UserID,s1,s2,s3,s4,s5,s6,s7,b1,b2,b3,b4,b5,b6,b7,day,w1,w2,w3,w4,w5,w6,w7,courseID,coursecount'+'\n')


    # f_out.write('dropout,s1,s2,s3,s4,s5,s6,s7,b1,b2,b3,b4,b5,b6,b7,day,w1,w2,w3,w4,w5,w6,w7,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,h21,h22,h23,h24,courseID,coursecount'+'\n')
    f_out.write('UserID,s1,s2,s3,s4,s5,s6,s7,b1,b2,b3,b4,b5,b6,b7,day,w1,w2,w3,w4,w5,w6,w7,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,h21,h22,h23,h24,courseID,coursecount'+'\n')


    for line in file_course:
        if line != '\n':

            infoList = line.split('\t')

            # extractList = []

            # p0 = infoList[0]
            # day = str(int(infoList[-3])==1)
            # course = infoList[-2]
            # count = infoList[-1]

            # extractList.append(p0)


            # #Key Feature Selection
            # s1 = int(infoList[1])
            # s2 = int(infoList[2])
            # s3 = int(infoList[3])
            # s4 = int(infoList[4])
            # s5 = int(infoList[5])
            # s6 = int(infoList[6])
            # s7 = int(infoList[7])

            # s_positive = str(s1+s2+s4+s5)

            # s_negative = str(s3)

            # s_navigate = str(s6)

            # s_close = str(s7)

            # extractList.append(s_positive)
            # extractList.append(s_negative)
            # extractList.append(s_navigate)
            # extractList.append(s_close)



            # b1 = int(infoList[8])
            # b2 = int(infoList[9])
            # b3 = int(infoList[10])
            # b4 = int(infoList[11])
            # b5 = int(infoList[12])
            # b6 = int(infoList[13])
            # b7 = int(infoList[14])

            # b_positive = str(b1+b2+b4+b5)

            # b_negative = str(b3)

            # b_navigate = str(b6)

            # b_close = str(b7)

            # extractList.append(b_positive)
            # extractList.append(b_negative)
            # extractList.append(b_navigate)
            # extractList.append(b_close)

            # extractList.append(day)
            # extractList.append(course)
            # extractList.append(count)



            outline = ''

            for item in infoList[:-1]:
            # for item in extractList[:-1
                outline += item+','
            outline += infoList[-1].strip()+'\n'
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

