# how many ways can you rename a file to new file name by deleting characters from old filename

def nPr(N):
    if N <= 1:
        return 1
    else:
        return N * nPr(N-1)

def renameFile(newName, oldName):
    # Write your code here
    r = len(newName)
    n = len(oldName)
    X = int(nPr(n)/(nPr(r) * nPr(n-r)))
    return X

    

#3! 2! 2! = 3x2x2x2 = 24 
#3/5 * 2/4 * 2/3 = 12/60 = 1/5

if __name__ == '__main__':
    n = renameFile("aba", "ababa")
    print(n)
