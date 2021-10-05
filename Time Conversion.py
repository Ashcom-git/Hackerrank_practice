#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(string_):
    # Write your code here
    # string_ = '07:05:45PM'
    hour = int(string_[:2])
    if string_[-2:] == 'PM':
        if hour != 12:
            return str(12+hour)+string_[2:-2]
        else:
            return '12'+string_[2:-2]
        
    else:
        if hour != 12:
            return string_[:-2]
        else:
            return '00'+string_[2:-2]  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
