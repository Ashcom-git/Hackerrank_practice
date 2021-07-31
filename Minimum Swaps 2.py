#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(a):
    cnt = 0
    for i in range(len(a)):
        if a[i]-1 != i:
            for j in range(i+1,len(a)):
                if a[j]-1 == i:
                    a[i],a[j] = a[j],a[i]
                    cnt += 1
                    break           
    return cnt
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
