import math

def prime_factors(n):
    factors = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i ad divide n
        while n % i== 0:
            factors.append(i)
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        factors.append(n)
    return factors

n1 = 52224
print(n1,"=", " x ".join(str(x) for x in prime_factors(n1)))

n2 = 202125
print(n2,"=", " x " .join(str(x) for x in prime_factors(n2)))

n3 = 117649
print(n3,"=", " x " .join(str(x) for x in prime_factors(n3)))