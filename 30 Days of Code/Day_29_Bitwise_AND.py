# Objective
# Welcome to the last day! Today, we're discussing bitwise operations. Check out the Tutorial tab for learning materials and an instructional video!

# Task
# Given set . Find two integers,  and  (where ), from set  such that the value of  is the maximum possible and also less than a given integer, . In this case,  represents the bitwise AND operator.

# Function Description
# Complete the bitwiseAnd function in the editor below.

# bitwiseAnd has the following paramter(s):
# - int N: the maximum integer to consider
# - int K: the limit of the result, inclusive

# Returns
# - int: the maximum value of  within the limit.

# Input Format

# The first line contains an integer, , the number of test cases.
# Each of the  subsequent lines defines a test case as  space-separated integers,  and , respectively.

# Constraints

# Sample Input

# STDIN   Function
# -----   --------
# 3       T = 3
# 5 2     N = 5, K = 2
# 8 5     N = 8, K = 5
# 2 2     N = 8, K = 5
# Sample Output

# 1
# 4
# 0
# Explanation

 

# All possible values of  and  are:

# The maximum possible value of  that is also  is , so we print  on a new line.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(N, K):
    # Write your code here
    maximum = 0
    for i in range(1,N+1):
        for j in range(1,i):
            h = i & j
            if maximum < h < K:
                maximum = h
            if maximum == K-1:
                return maximum
    return maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()