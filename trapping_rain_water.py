import sys


def trap_rain_water(arr):
    n = len(arr)
    trapped = [0] * n
    left_arr = [0] * n
    right_arr = [0] * n

    max_left = -sys.maxsize
    max_right = -sys.maxsize
    for i in range(n):
        j = n - i - 1
        left, right = arr[i], arr[j]
        max_left, max_right = max(max_left, left), max(max_right, right)
        left_arr[i], right_arr[j] = max_left, max_right

    for i, (left, right) in enumerate(zip(left_arr, right_arr)):
        trapped[i] = min(left, right) - arr[i]

    return sum(trapped)


if __name__ == '__main__':
    data = [
        [1, 0, 2, 0, 1, 0, 3, 1, 0, 2], [3, 0, 2, 0, 4]
    ]
    for arr in data:
        trapped_rain_water = trap_rain_water(arr)
        print(f'trapped rain water {arr} ==> {trapped_rain_water} units')
