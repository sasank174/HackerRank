# HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, they advertise it to exactly  people on social media.

# On the first day, half of those  people (i.e., ) like the advertisement and each shares it with  of their friends. At the beginning of the second day,  people receive the advertisement.

# Each day,  of the recipients like the advertisement and will share it with  friends on the following day. Assuming nobody receives the advertisement twice, determine how many people have liked the ad by the end of a given day, beginning with launch day as day .

# Example
# .

# Day Shared Liked Cumulative
# 1      5     2       2
# 2      6     3       5
# 3      9     4       9
# 4     12     6      15
# 5     18     9      24
# The progression is shown above. The cumulative number of likes on the  day is .

# Function Description

# Complete the viralAdvertising function in the editor below.

# viralAdvertising has the following parameter(s):

# int n: the day number to report
# Returns

# int: the cumulative likes at that day
# Input Format

# A single integer, , the day number.

# Constraints

# Sample Input

# 3
# Sample Output

# 9
# Explanation

# This example is depicted in the following diagram:

# strange ad.png

#  people liked the advertisement on the first day,  people liked the advertisement on the second day and  people liked the advertisement on the third day, so the answer is .



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def viralAdvertising(n):
    # Write your code here
    li,l,s = 0,0,5
    for i in range(n):
        l = s//2
        s,li = l*3,li+l
    return li

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
