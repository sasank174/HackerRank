# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:

# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  
# Function Description

# Complete the swap_case function in the editor below.

# swap_case has the following parameters:

# string s: the string to modify
# Returns

# string: the modified string
# Input Format

# A single line containing a string .

# Constraints


# Sample Input 0

# HackerRank.com presents "Pythonist 2".
# Sample Output 0

# hACKERrANK.COM PRESENTS "pYTHONIST 2".

def swap_case(s):
    swap = ""
    
    for i in s:
        if i.isupper():
            swap+= i.lower()
        else:
            swap+= i.upper()
    
    return swap

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)