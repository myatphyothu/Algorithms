# There is a string, s='abcac', of lowercase English letters that is repeated infinitely many times. 
# Given an integer n , find and print the number of letter a's in the first  
# letters of the infinite string.

# Example
# s = 'abcac'
# n = 10

# The substring we consider is 'abcacabcac, the first 10 characters of the infinite string. 
# There are 4 occurrences of a in the substring.

# Complete the repeatedString function below.
# look for a
def repeatedString(s, n):
    L = len(s)
    a = len([c for c in s if c == 'a']) # total a in s
    
    R = n % L # the extra characters
    K = n - R # N repeated times

    count = int(K/L) * a + (0 if R == 0 else len([c for c in range(R) if s[c] == 'a']))
    
    return count
    

if __name__ == '__main__':
    s = 'aab'
    n = 882787
    
    result = repeatedString(s,n)

    print(result)