
def diagonal_diff(arr):
    sq_num = len(arr)
    sum1 = 0
    sum2 = 0
    for i in range(sq_num):
        sum1 += arr[i][i]
        sum2 += arr[i][-(i+1)]
    return abs(sum1 - sum2)


if __name__ == '__main__':
    arr = [
        [1, 2, 3],
        [3, 4, 5],
        [5, 6, 7]
    ]
    arr2 = [
        [1, 2, 3, 4],
        [4, 5, 6, 7],
        [7, 8, 9, 10],
        [10, 11, 12, 13]
    ]
    print(diagonal_diff(arr))
    print(diagonal_diff(arr2))
