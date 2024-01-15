def reverse(N):
    R = 0
    while N > 0:
        R = R*10 + (N%10)
        N /= 10
    return R


print(123, reverse(123))
print(44778, reverse(44778))