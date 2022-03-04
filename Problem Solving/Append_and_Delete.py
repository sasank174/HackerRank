# You have two strings of lowercase English letters. You can perform two types of operations on the first string:

# Append a lowercase English letter to the end of the string.
# Delete the last character of the string. Performing this operation on an empty string results in an empty string.
# Given an integer, , and two strings,  and , determine whether or not you can convert  to  by performing exactly  of the above operations on . If it's possible, print Yes. Otherwise, print No.

# Example. 


# To convert  to , we first delete all of the characters in  moves. Next we add each of the characters of  in order. On the  move, you will have the matching string. Return Yes.

# If there were more moves available, they could have been eliminated by performing multiple deletions on an empty string. If there were fewer than  moves, we would not have succeeded in creating the new string.

# Function Description

# Complete the appendAndDelete function in the editor below. It should return a string, either Yes or No.

# appendAndDelete has the following parameter(s):

# string s: the initial string
# string t: the desired string
# int k: the exact number of operations that must be performed
# Returns

# string: either Yes or No
# Input Format

# The first line contains a string , the initial string.
# The second line contains a string , the desired final string.
# The third line contains an integer , the number of operations.

# Constraints

#  and  consist of lowercase English letters, .
# Sample Input 0

# hackerhappy
# hackerrank
# 9
# Sample Output 0

# Yes
# Explanation 0

# We perform  delete operations to reduce string  to hacker. Next, we perform  append operations (i.e., r, a, n, and k), to get hackerrank. Because we were able to convert  to  by performing exactly  operations, we return Yes.

# Sample Input 1

# aba
# aba
# 7
# Sample Output 1

# Yes
# Explanation 1

# We perform  delete operations to reduce string  to the empty string. Recall that though the string will be empty after  deletions, we can still perform a delete operation on an empty string to get the empty string. Next, we perform  append operations (i.e., a, b, and a). Because we were able to convert  to  by performing exactly  operations, we return Yes.

# Sample Input 2

# ashley
# ash
# 2
# Sample Output 2

# No
# Explanation 2

# To convert ashley to ash a minimum of  steps are needed. Hence we print No as answer.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    s,t = list(s),list(t)
    i = 0
    
    while i<len(s) and i<len(t) and s[i]==t[i]:i+=1
    
    s1 = len(s[i:])
    t1 = len(t[i:])
    if s1+t1>k:return "No"
    elif s1+t1==k or (len(s)+len(t))-k<=0 or abs((len(s)+len(t))-k)%2==0:return "Yes"
    else:return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
