# ugly numbers are those whose only prime factors are 2,3 or 5.

import os,sys

def get_nth_ugly_number(N):
    ugly_array = [0]*N
    ugly_array[0] = 1

    i2 = i3 = i5 = 0

    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    # find value from ugly_array[1] to ugly_array[N]
    for x in range(1, N):
        ugly_array[x] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)

        # increment the value of index accordingly
        if ugly_array[x] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly_array[i2] * 2
        
        if ugly_array[x] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly_array[i3] * 3

        if ugly_array[x] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly_array[i5] * 5

    return ugly_array[-1]

if __name__ == '__main__':
    script,arg = sys.argv

    print (arg)