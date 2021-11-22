# Objective
# Today, we are learning about an algorithmic concept called recursion. Check out the Tutorial tab for learning materials and an instructional video.

# Recursive Method for Calculating Factorial
# Function Description
# Complete the factorial function in the editor below. Be sure to use recursion.

# factorial has the following paramter:

# int n: an integer
# Returns

# int: the factorial of 
# Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of .

# Input Format

# A single integer,  (the argument to pass to factorial).

# Constraints

# Your submission must contain a recursive function named factorial.
# Sample Input

# 3
# Sample Output

# 6
# Explanation

# Consider the following steps. After the recursive calls from step 1 to 3, results are accumulated from step 3 to 1.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here
    fac = 1
    for i in range(1,n+1):
        fac = fac*i
    return fac
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
