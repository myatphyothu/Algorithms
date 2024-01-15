
def S(A):
    if len(A) == 0:
        return 0
    else:
        return A.pop(0) + S(A)

if __name__ == "__main__":
    A = [1,2,3]
    print(S(A))