# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to .

# Example


# There are two subarrays meeting the criterion:  and . The maximum length subarray has  elements.

# Function Description

# Complete the pickingNumbers function in the editor below.

# pickingNumbers has the following parameter(s):

# int a[n]: an array of integers
# Returns

# int: the length of the longest subarray that meets the criterion
# Input Format

# The first line contains a single integer , the size of the array .
# The second line contains  space-separated integers, each an .

# Constraints

# The answer will be .
# Sample Input 0

# 6
# 4 6 5 3 3 1
# Sample Output 0

# 3
# Explanation 0

# We choose the following multiset of integers from the array: . Each pair in the multiset has an absolute difference  (i.e.,  and ), so we print the number of chosen integers, , as our answer.

# Sample Input 1

# 6
# 1 2 2 3 1 2
# Sample Output 1

# 5
# Explanation 1

# We choose the following multiset of integers from the array: . Each pair in the multiset has an absolute difference  (i.e., , , and ), so we print the number of chosen integers, , as our answer.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    ans=0
    for i in range(len(a)):
        for j in range(len(a)):
            if abs(a[j] - a[i]) <= 1:ans = max(ans, j - i + 1)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
