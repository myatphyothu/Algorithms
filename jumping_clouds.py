# find the shortest number of jumps 
# the maximum jump that can be performed is 2
# must avoid indices that has values of 1
# only 0s are safe to land

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    L = len(c)
    jumps = 0
    i = 0
    while True:
        if i + 2 < L:
            if c[i+2] == 0:
                
                i += 2
                jumps += 1
                
            elif c[i+1] == 0:
                i += 1
                jumps += 1
            else:
                # impossible to jump
                return -1
        elif i + 1 < L:
            
            if c[i+1] == 0:
                i += 1
                jumps += 1
            else:
                # impossible to jump
                return -1
        else:
            # end
            break

        if i >= L: break
    return jumps
            
        
                    
if __name__ == '__main__':
    c = [0,0,1,0,0,1,0]

    
    result = jumpingOnClouds(c)

    print(result)