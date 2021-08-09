#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def count(val):
  y = dict()
  for i in val:
    if i not in y.keys():
      y[i] = 1
    else:
      y[i] = y[i]+1    
  return y

def checkMagazine(magazine, notes):
    mag = count(magazine)
    note = count(notes)
    flag = False
    for j in note.keys():
        if j in mag.keys() and note[j] <= mag[j]:
            flag = True
        else:
            flag = False
            break  

    if flag:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
