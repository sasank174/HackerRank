# John Watson knows of an operation called a right circular rotation on an array of integers. One rotation operation moves the last array element to the first position and shifts all remaining elements right one. To test Sherlock's abilities, Watson provides Sherlock with an array of integers. Sherlock is to perform the rotation operation a number of times then determine the value of the element at a given position.

# For each array, perform a number of right circular rotations and return the values of the elements at the given indices.

# Example



# Here  is the number of rotations on , and  holds the list of indices to report. First we perform the two rotations: 

# Now return the values from the zero-based indices  and  as indicated in the  array.


# Function Description

# Complete the circularArrayRotation function in the editor below.

# circularArrayRotation has the following parameter(s):

# int a[n]: the array to rotate
# int k: the rotation count
# int queries[1]: the indices to report
# Returns

# int[q]: the values in the rotated  as requested in 
# Input Format

# The first line contains  space-separated integers, , , and , the number of elements in the integer array, the rotation count and the number of queries.
# The second line contains  space-separated integers, where each integer  describes array element  (where ).
# Each of the  subsequent lines contains a single integer, , an index of an element in  to return.

# Constraints

# Sample Input 0

# 3 2 3
# 1 2 3
# 0
# 1
# 2
# Sample Output 0

# 2
# 3
# 1
# Explanation 0

# After the first rotation, the array is .
# After the second (and final) rotation, the array is .

# We will call this final state array . For each query, we just have to get the value of .

# , .
# , .
# , .




#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # Write your code here
    for i in range(k):
        x = a.pop()
        a.insert(0,x)
    return [a[i] for i in queries]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
