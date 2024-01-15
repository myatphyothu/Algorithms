'''
Given a range of numbered days [i...j],  and a number k, determine the number of days in the range that are beautiful. 
Beautiful numbers are defined as numbers where  is evenly divisible by k. If a day's value is a beautiful number, it is a beautiful day. Return the number of beautiful days in the range.
'''

def beautiful_days(i,j,k):
    
    def reverse(n):
        R = 0
        while n != 0:
            remainder = n%10
            R = R*10 + remainder
            n //= 10
       
        return R

    c = 0
    for x in range(i,j+1):

        if (i-reverse(i)) % k == 0:
            c += 1
    
    return c


