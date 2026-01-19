#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # store1, store2 = s.split(' ')
    # fname = store1[0].upper() + store1[1:]
    # lname = store2[0].upper() + store2[1:]
    
    # result = fname +' '+ lname
    
    # result = s.title()
    # return result
    
    return " ".join([i.capitalize() for i in s.split(" ")])
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
