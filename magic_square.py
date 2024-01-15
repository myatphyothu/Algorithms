# a magic square is a NxN matrix where the sum of any row, column or diagonal length N
# is always equal to the same number, the magic constant

# the resulting magic square contains distinct integers from range [1,9]

import math
import os
import random
import re
import sys

#magic square constant of size n = n x (n^2 + 1)/2 

# 8 1 6
# 3 5 7
# 4 9 2

# 5 3 4
# 1 5 8
# 6 4 2

def magic_square(N):
    

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    pre = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        ]
    results = []

    for p in pre:
        for p_row, s_row in zip(p, s):
            print(p_row, s_row)
        
    
    return 0


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = [[5,3,4], [1,5,8], [6,4,2]]

    result = formingMagicSquare(s)
    print (result)

    #fptr.write(str(result) + '\n')

    #fptr.close()