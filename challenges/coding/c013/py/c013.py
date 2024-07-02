def findMedian(arr):
    arr.sort()
    middle_index = len(arr) // 2
    return arr[middle_index]

arr = [5, 3, 1, 2, 4]
print(findMedian(arr))  # Output: 3
