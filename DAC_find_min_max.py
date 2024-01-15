def DAC_find_min(A, index, L):
    min = 0

    if index >= L - 2:
        print(index)
        return A[index] if A[index] < A[index+1] else A[index+1]
    
    min = DAC_find_min(A,index + 1,L)
    return A[index] if A[index] < min else min

if __name__ == "__main__":
    A = [70,250,50,80,140,12,14]
    
    min = DAC_find_min(A,0,len(A))
    print(A)
    print("min:",min)