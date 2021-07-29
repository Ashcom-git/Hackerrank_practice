#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(num,lst):

    flag = False
    abc = 0
    for i in range(len(lst)):
        if lst[i]-(i+1)>2:
            flag = True
            break
        else:
            for j in range(max(0,lst[i]-2),i):
              if lst[j]>lst[i]:
                abc += 1
    if flag:   
        print('Too chaotic')
    else:     
        print(abc)        
    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(n,q)
