#!/bin/bash

import time
import argparse

# Argparser
parser=argparse.ArgumentParser(description="Efficient mehtod: memoritation tool has been implemented to improve the runtime")
parser.add_argument('-n','--fibint', type=int, required=True, help='the n-th number for the fibonacci function')
group = parser.add_mutually_exclusive_group()
group.add_argument('-all', '--allnumbers', action='store_true',help='returns a comma separated list of all fibo-numbers')
args = parser.parse_args()
inp_numb = args.fibint

# Dictionary to cache values
temp_fibo = {}

# Funktion
def fibo(n):
    """Calculates fibonacci numbers ineffiently"""
    if n in temp_fibo:
        return temp_fibo[n]

    if n == 1 or n == 2:
        return 1

    else:
        f = (fibo(n-1) + fibo(n-2))
        # return(f)

    temp_fibo[n] = f
    return f


start_time = time.perf_counter()

# Funktionsaufruf:
if args.allnumbers:
    fiboList = []
    for i in range(1, inp_numb+1):
        fiboList.append(fibo(i))
    print(fiboList)

else:
    print(fibo(inp_numb))

end_time = time.perf_counter()
#print("Program duration: ", end_time-start_time, "sec.")