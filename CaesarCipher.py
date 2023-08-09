#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    cipher = ""
    for letter in s:
        if not letter.isalpha():
            cipher += letter
        
        else:
            ascii = ord(letter) + k

            while (letter.isupper() and ascii > 90) or ascii > 122:
                ascii -= 26

            cipher += chr(ascii)

    return cipher

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
