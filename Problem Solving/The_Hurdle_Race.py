# A video player plays a game in which the character competes in a hurdle race. Hurdles are of varying heights, and the characters have a maximum height they can jump. There is a magic potion they can take that will increase their maximum jump height by  unit for each dose. How many doses of the potion must the character take to be able to jump all of the hurdles. If the character can already clear all of the hurdles, return .

# Example


# The character can jump  unit high initially and must take  doses of potion to be able to jump all of the hurdles.

# Function Description

# Complete the hurdleRace function in the editor below.

# hurdleRace has the following parameter(s):

# int k: the height the character can jump naturally
# int height[n]: the heights of each hurdle
# Returns

# int: the minimum number of doses required, always  or more
# Input Format

# The first line contains two space-separated integers  and , the number of hurdles and the maximum height the character can jump naturally.
# The second line contains  space-separated integers  where .

# Constraints

# Sample Input 0

# 5 4
# 1 6 3 5 2
# Sample Output 0

# 2
# Explanation 0

# Dan's character can jump a maximum of  units, but the tallest hurdle has a height of :

# image

# To be able to jump all the hurdles, Dan must drink  doses.

# Sample Input 1

# 5 7
# 2 5 4 5 2
# Sample Output 1

# 0
# Explanation 1

# Dan's character can jump a maximum of  units, which is enough to cross all the hurdles:

# image

# Because he can already jump all the hurdles, Dan needs to drink  doses.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    # Write your code here
    count=0
    for i in height:
        if i>k:
            count+=i-k
            k=i
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()