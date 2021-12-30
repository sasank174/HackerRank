# When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently. For example:

# PDF-highighting.png

# There is a list of  character heights aligned by index to their letters. For example, 'a' is at index  and 'z' is at index . There will also be a string. Using the letter heights given, determine the area of the rectangle highlight in  assuming all letters are  wide.

# Example
 

# The heights are  and . The tallest letter is  high and there are  letters. The hightlighted area will be  so the answer is .

# Function Description

# Complete the designerPdfViewer function in the editor below.

# designerPdfViewer has the following parameter(s):

# int h[26]: the heights of each letter
# string word: a string
# Returns

# int: the size of the highlighted area
# Input Format

# The first line contains  space-separated integers describing the respective heights of each consecutive lowercase English letter, ascii[a-z].
# The second line contains a single word consisting of lowercase English alphabetic letters.

# Constraints

# , where  is an English lowercase letter.
#  contains no more than  letters.
# Sample Input 0

# 1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
# abc
# Sample Output 0

# 9
# Explanation 0

# We are highlighting the word abc:

# Letter heights are ,  and . The tallest letter, b, is  high. The selection area for this word is .

# Note: Recall that the width of each character is .

# Sample Input 1

# 1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
# zaba
# Sample Output 1

# 28
# Explanation 1

# The tallest letter in  is  at . The selection area for this word is .

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    numbers = [h[(ord(x) - 97)] for x in word]
    return len(numbers)*max(numbers)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()