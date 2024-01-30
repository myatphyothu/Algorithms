import sys


def kadane_algorithm_subarray_with_max_sum(arr, debug=False):

    if len(arr) == 1:
        return arr
    elif len(arr) == 0:
        return []
    else:
        start = 0
        end = 0
        max_sum = arr[0]
        prev_element = arr[0]
        curr_sum = arr[0]
        master_max_sum = arr[0]
        master_start, master_end = 0, 0

        for i, curr_element in enumerate(arr[1:]):
            i = i + 1
            print(f'==== [{i}] | prev_element:{prev_element} | curr_element:{curr_element} | max_sum:{max_sum} | start:{start} | end:{end}') if debug is True else ()
            curr_sum += curr_element
            if curr_sum == 0:
                master_max_sum = max_sum
                master_start, master_end = start, end
                start, end = i, i

            print(f'curr_sum += curr_element = {curr_sum}') if debug is True else ()

            if curr_element >= curr_sum and curr_element > max_sum and curr_element > master_max_sum:
                print(f'True: curr_element > curr_sum and curr_element > max_sum') if debug is True else ()
                start = i
                end = i
                max_sum = curr_element
                curr_sum = max_sum
                master_start, master_end = start, end

            elif curr_sum > max_sum and curr_sum > master_max_sum:
                if debug is True:
                    print(f'False: curr_element > curr_sum')
                    print(f'True: curr_sum > max_sum')
                max_sum = curr_sum
                master_max_sum = max_sum
                end = i
                master_start, master_end = start, end

            print(f'start = {start}, end = {end}, max_sum = {max_sum} =====') if debug is True else ()
            prev_element = curr_element

        return arr[master_start:master_end+1]


if __name__ == '__main__':
    data = [
        [-2, 2, 5, -11, 6],
        [-9, 0, 8, -4, 33, -2, 5, -40, 0, 99, -5]
    ]
    for arr in data:
        subarray = kadane_algorithm_subarray_with_max_sum(arr)
        print(f'{arr}: the subarray with max sum is {subarray}')
