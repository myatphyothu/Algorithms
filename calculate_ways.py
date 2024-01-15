

def calculateWays(wordLen, maxVowels):

    
    # Write your code here
    def fac(N):
        if N <= 1:
            return 1
        else:
            return N * fac(N-1)

    def nPr(n, r):
        return int(fac(n) / fac(n-r))
    
    def nCr(n, r):
        return int(fac(n)/(fac(r) * fac(n-r)))

    def nCr_repetition(n,r):
        return int(fac(n+r-1) / (fac(r) * fac(n-1)) )
    
    c = 21
    v = 5
    X = 0

    
    X1 = c**wordLen
    print("X1", X1)

    X2 = 0
    for i in range(wordLen):
        X2 += c**(wordLen-i) * v**i
    
    print("X2", X2)


    # N = 0
    
    # X3_list = []
    # K = 1
    # while N < wordLen:
        
    #     i = N
    #     x = 0
    #     used = maxVowels

    #     while x < N:
    #         K *= c
    #         print('c',end='')
            
    #         x += 1

    #     while i < wordLen:
        
    #         if used > 0:
    #             K *= v
    #             print('v', end='')
    #             used -= 1
    #         else:
                
    #             print('c', end='')
    #             K *= c
    #             used += 1

    #         i += 1
    #     print(' ', K, end= '')
    #     N += 1
    #     X3_list.append(K)
        
    #     print()
    #     K = 1

    # X3 = sum(X3_list)   

        
    
        
    #X3 = nPr(wordLen, maxVowels+1) * (c**(wordLen-(maxVowels+1)) * v**(maxVowels-1))
    X3 = nCr_repetition(wordLen,maxVowels) * (c**(wordLen-(maxVowels+1)) * v**(maxVowels-1))
    print("X3", X3)
    

    #X = arrangements * (c**(wordLen-maxVowels) * v**(maxVowels))
    X = X1 + X2 + X3

    #print(nCr(7,3))
    
    

    return X


if __name__ == '__main__':

    wordLen = 4

    maxVowels = 1

    result = calculateWays(wordLen, maxVowels)

    print(result)