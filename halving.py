
def halve_this(n, cnt, arr):
    if n > 2:
        v = n // 2
        arr.append(v)
        return halve_this(v, cnt + 1, arr)
    else:
        return cnt, arr


if __name__ == '__main__':
    data = [100, 80, 60, 50, 20, 10]
    data2 = [796723]
    for n in data2:
        cnt, halves = halve_this(n=n, cnt=0, arr=[n])
        print(f'{n} ==> cnt: {cnt}, {halves}')

