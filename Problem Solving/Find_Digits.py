# An integer  is a divisor of an integer  if the remainder of .

# Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.

# Example

# Check whether ,  and  are divisors of . All 3 numbers divide evenly into  so return .


# Check whether , , and  are divisors of . All 3 numbers divide evenly into  so return .


# Check whether  and  are divisors of .  is, but  is not. Return .

# Function Description

# Complete the findDigits function in the editor below.

# findDigits has the following parameter(s):

# int n: the value to analyze
# Returns

# int: the number of digits in  that are divisors of 
# Input Format

# The first line is an integer, , the number of test cases.
# The  subsequent lines each contain an integer, .

# Constraints



# Sample Input

# 2
# 12
# 1012
# Sample Output

# 2
# 3
# Explanation

# The number  is broken into two digits,  and . When  is divided by either of those two digits, the remainder is  so they are both divisors.

# The number  is broken into four digits, , , , and .  is evenly divisible by its digits , , and , but it is not divisible by  as division by zero is undefined.



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    
    s = [int(i) for i in str(n)]
    count=0
    for i in s:
        if i == 0:continue
        elif n%i == 0:count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
