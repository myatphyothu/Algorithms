# pick the longest subarray where the absolute difference between any two elements is 
# less than or equal to 1

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
    def sub_arrays(a):

        # sort a
        a = sorted(a)
        K = []
        # loop until a is empty
        while len(a) > 0:
            x, y = a[0], None
            t_x = a.count(x)
            k = [x] * t_x

            y = x + 1
            t_y = a.count(y)
            if t_y >= 1:
                k += [y] * t_y
            else:
                y = x - 1
                t_y = a.count(y)
                if t_y >= 1:
                    k += [y] * t_y
            
            a = list(filter(lambda n: n != x, a))
            if not y is None:
                a = list(filter(lambda n: n != y, a))
            
            K.append(k)

        return K

    X = sub_arrays(a)
    return max([len(x) for x in X])
        

if __name__ == "__main__":
    
    A = [1,1,2,2,4,4,5,5,5]
    # [1,1,2,2] and [4,4,5,5,5]: pick [4,4,5,5,5]
    print ("input", A)
    print (pickingNumbers(A))

    
    B = [4,6,5,3,3,1]
    # [4,3,3]
    print ("input", B)
    print (pickingNumbers(B))