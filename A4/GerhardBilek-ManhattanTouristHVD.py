#!/Users/gerhardbilek/anaconda3/bin/python3

import sys

'''
execute program:
$githubusername-ManhattanTouristHV.$suffix < rmHV_10_5
python3.7 mt.py < rmHVD_10_15 

Testmatrizen:
rmHVD_10_15 (weight = 61.34)
rmHVD_999_15 (weight = 7220.98)  Korrekt: 7221.69
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
print("Dimension: ", columns, rows)  # TEST

#__ initialize storing matrix with 0
countMatrix={}
for i in range(rows):
    countMatrix[i]=[]
    for j in range(columns):
        countMatrix[i].append(0)

#print(theList[rows-1]) # startRightMatrix
#print(theList[2*rows-1]) #startDiagonalMatrix

#__ calc FIRST right
for i in range(rows-1):
    countMatrix[0][i+1] = countMatrix[0][i] + float(theList[rows-1][i])

#__ calc FIRST down
for i in range(columns-1):
    countMatrix[i+1][0] = countMatrix[i][0] + float(theList[i][0])



#__ Manhattan
for j in range(rows-1):       
        for i in range(columns-1):
                #__ DOWN
                down = countMatrix[j][i+1]+ float(theList[j][i+1])
                #print("D_countMatrix: ", countMatrix[j][i+1])
                #print("D_theList: ", theList[j][i+1])
                #print("Down_sum",down)
                #__ RIGHT
                right = countMatrix[j+1][i]+ float(theList[rows+j][i])
                #print("R_countMatrix: ", countMatrix[j+1][i])
                #print("R_theList: ", theList[rows+j][i])
                #print("right_sum", right)
                #__ DIAGONAL
                diagonal = countMatrix[j][i]+ float(theList[2*rows-1+j][i])
                #print("Dia_countMatrix: ", countMatrix[j][i])
                #print("Dia_theList: ", theList[2*rows-1+j][i])
                #print("Dia_sum", diagonal)

                if (down >= right and down >= diagonal):
                        countMatrix[j+1][i+1] = down
                elif (right > down and right >= diagonal):
                        countMatrix[j+1][i+1] = right
                elif (diagonal > down and diagonal > right):
                        countMatrix[j+1][i+1] = diagonal


# TestMatrix 20.68

#__ print countMatrix per line
#for i in range(len(countMatrix)):
#        print(countMatrix[i])


print(countMatrix[rows-1][columns-1])

