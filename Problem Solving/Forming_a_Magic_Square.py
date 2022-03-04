# We define a magic square to be an  matrix of distinct positive integers from  to  where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.

# You will be given a  matrix  of integers in the inclusive range . We can convert any digit  to any other digit  in the range  at cost of . Given , convert it into a magic square at minimal cost. Print this cost on a new line.

# Note: The resulting magic square must contain distinct integers in the inclusive range .

# Example

# $s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

# The matrix looks like this:

# 5 3 4
# 1 5 8
# 6 4 2
# We can convert it to the following magic square:

# 8 3 4
# 1 5 9
# 6 7 2
# This took three replacements at a cost of .

# Function Description

# Complete the formingMagicSquare function in the editor below.

# formingMagicSquare has the following parameter(s):

# int s[3][3]: a  array of integers
# Returns

# int: the minimal total cost of converting the input square to a magic square
# Input Format

# Each of the  lines contains three space-separated integers of row .

# Constraints

# Sample Input 0

# 4 9 2
# 3 5 7
# 8 1 5
# Sample Output 0

# 1
# Explanation 0

# If we change the bottom right value, , from  to  at a cost of ,  becomes a magic square at the minimum possible cost.

# Sample Input 1

# 4 8 2
# 4 5 7
# 6 1 6
# Sample Output 1

# 4
# Explanation 1

# Using 0-based indexing, if we make

# -> at a cost of 
# -> at a cost of 
# -> at a cost of ,
# then the total cost will be .


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    orig = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    all_squares = [orig]
    all_squares.append(orig[::-1])
    all_squares.append([i[::-1] for i in orig])
    all_squares.append(all_squares[2][::-1])
    all_squares.append([[4, 3, 8], [9, 5, 1], [2, 7, 6]])
    all_squares.append(all_squares[4][::-1])
    all_squares.append([i[::-1] for i in all_squares[4]])
    all_squares.append(all_squares[6][::-1])
    
    least = 99
    for i in all_squares:
        temp = 0
        for j in range(3):
            for k in range(3):
                temp += abs(s[j][k]-i[j][k])
        if temp < least:
            least = temp

    return least

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
