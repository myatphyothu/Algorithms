def insertionSort(arr):

    steps = 0
    comparisons = 0
    swaps = 0
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        steps += 1

        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1

        # while j >= 0:
        #     comparisons += 1
        #     if key < arr[j]:
        #         arr[j+1] = arr[j]
        #         swaps += 1

        #     j -= 1

        while j >= 0 and key < arr[j] :
                
                swaps += 1
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    print("swaps", swaps)
 
# Driver code to test above
arr = [19,1,3,7,9,11,13,15,16,18]
print(arr)
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])