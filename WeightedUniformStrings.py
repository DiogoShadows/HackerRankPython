#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    currentChar = ''
    currentSum = 0
    dictWeights = {}

    for letter in s:
        valueLetter = ord(letter) - 96
        
        if letter != currentChar:
            currentChar = letter
            currentSum = valueLetter

        else:
            currentSum += valueLetter

        if currentSum not in dictWeights:
            dictWeights[currentSum] = 0
    
    result = []

    for query in queries:
        result.append("Yes" if query in dictWeights else "No")

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
