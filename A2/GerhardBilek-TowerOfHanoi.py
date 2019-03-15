#!/bin/bash

import argparse
import sys

# Argparser
parser=argparse.ArgumentParser(description="Recursive calls are performed to describe Tower of Hanoi moves")
parser.add_argument('-n','--plateAmount', type=int, required=True, help='Enter the amount of plates used for the Hanoi Tower')
args = parser.parse_args()
n = args.plateAmount   # argparse container

count= 0               # storing the recursive calls of the function

def hanoi(n, start, aux, dest):
    global count
    if n == 1:
        print(f"Move dis from {start} to {dest}")   # print ot STDOUT
        count += 1
    else:
        hanoi(n-1, start, dest, aux)
        count += 1
        print(f"Move disc from {start} to {dest}")  # print to STDOUT
        hanoi(n-1, aux, start, dest)

hanoi(n, "A", "B", "C")        # call of function
print(count, file=sys.stderr)  # print total number of disc move operations in STDERR

## Notes:
## Example call on CLI:
# time python toh.py -n 2 2>log.txt 1>kombi.txt
# time python3 toh.py -n 3 > moves.txt
## Redirect:
# 2> ... Ausgabe des Errors in ein File
# 1> ... Ausgabe des STDOUT in ein File
# >> ... append
# > ... neu anlegen
