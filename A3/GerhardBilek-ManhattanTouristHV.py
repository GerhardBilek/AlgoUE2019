#!/bin/bash

import sys

'''
execute program:
$githubusername-ManhattanTouristHV.$suffix < rmHV_10_5
python3.7 mt.py < rmHV_10_15 

Testmatrizen:
rmHV_10_15 (weight = 13.53)
rmHV_999_15 (weight = 1565.71)
'''

theMatrix = sys.stdin
theList = []
matrixDimension = []
theMatrix.readline()

# Store the weights in a nested list
for row in theMatrix.readlines():
        weight = row.strip("  ").strip(" \n").split("   ")
        
        if (len(weight) > 1):
            #print(weight) #TEST
            rowLength = len(weight)
            theList.append(weight)

#__ matrix dimension
columns = len(theList[0])
columnAmount = len(theList)
rows = len(theList[columnAmount-1])+1
#print("Dimension: ", columns, rows)  # TEST

#__ initialize storing matrix with 0
countMatrix={}
for i in range(rows):
    countMatrix[i]=[]
    for j in range(columns):
        countMatrix[i].append(0)

#__ calc FIRST right
for i in range(rows-1):
    countMatrix[0][i+1] = round(countMatrix[0][i] + float(theList[rows-1][i]),2)

#__ calc FIRST down
for i in range(columns-1):
    countMatrix[i+1][0] = round(countMatrix[i][0] + float(theList[i][0]),2)

#__ Manhattan
for j in range(rows-1):       
        for i in range(columns-1):
                #__ DOWN
                down = round(countMatrix[j][i+1]+ float(theList[j][i+1]),2)
                #print("D_countMatrix: ", countMatrix[j][i+1])
                #print("D_theList: ", theList[j][i+1])
                #print("Down_sum",down)
                #__ RIGHT
                right = round(countMatrix[j+1][i]+ float(theList[rows+j][i]),2)
                #print("R_countMatrix: ", countMatrix[j+1][i])
                #print("R_theList: ", theList[rows+j][i])
                #print("right_sum", right)
                if (down > right):
                        countMatrix[j+1][i+1] = down
                else:
                        countMatrix[j+1][i+1] = right

#__ print countMatrix per line
#for i in range(len(countMatrix)):
#        print(countMatrix[i])

print(countMatrix[rows-1][columns-1])

