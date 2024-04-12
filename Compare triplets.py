#a=[1,5,8]
#b=[2,5,2]
# compare a[0] and b[0] is a is great ascore+1 else bscore+1
#o/p: [1,1] -> first is a score, second b score


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    aScore = 0
    bScore = 0
    for i, j in zip(a, b):
        if i<j:
            bScore += 1
        elif i>j:
            aScore += 1
    return [aScore, bScore]
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
