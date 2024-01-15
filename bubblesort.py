def bubbleSort(arr):
    steps = 0
    comparisons = 0
    swaps = 0

    n = len(arr)
  
    # Traverse through all array elements
    for i in range(n):
        steps += 1
        # Last i elements are already in place
        for j in range(0, n-i-1):
            comparisons += 1
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                swaps += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
    
    print("steps =", steps)
    print("comparisons =", comparisons)
    print("swaps =", swaps)
  
# Driver code to test above
arr = [14,71,52,25,36,17]
  
bubbleSort(arr)
  
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]), 