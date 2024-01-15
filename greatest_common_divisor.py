

def gcd(x,y):
    if x != 0 and y != 0:
        q = x//y
        r = x - (y*q)
        print('x')
        return gcd(y,r)
    else:
        if x == 0: return y
        return x

#print("gcd(8286,228) =", gcd(8286,228))
#print("gcd(191,139) =", gcd(191,139))
print(gcd(41,12))