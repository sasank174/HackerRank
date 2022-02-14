# There is a string, , of lowercase English letters that is repeated infinitely many times. Given an integer, , find and print the number of letter a's in the first  letters of the infinite string.

# Example


# The substring we consider is , the first  characters of the infinite string. There are  occurrences of a in the substring.

# Function Description

# Complete the repeatedString function in the editor below.

# repeatedString has the following parameter(s):

# s: a string to repeat
# n: the number of characters to consider
# Returns

# int: the frequency of a in the substring
# Input Format

# The first line contains a single string, .
# The second line contains an integer, .

# Constraints

# For  of the test cases, .
# Sample Input

# Sample Input 0

# aba
# 10
# Sample Output 0

# 7
# Explanation 0
# The first  letters of the infinite string are abaabaabaa. Because there are  a's, we return .

# Sample Input 1

# a
# 1000000000000
# Sample Output 1

# 1000000000000
# Explanation 1
# Because all of the first  letters of the infinite string are a, we return .



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    no = (n//len(s))*s.count('a')
    n = n%len(s)
    no+=s[:n].count('a')
    return no

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

# code by sasank174
# for more visit https://github.com/sasank174