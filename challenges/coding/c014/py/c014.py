def countingSort(arr):
    freq = [0] * 100
    
    for num in arr:
        freq[num] += 1
    
    return freq

# Example usage
arr = [1, 1, 3, 2, 1]
print(countingSort(arr))  # Output: [0, 3, 1, 1, 0, 0, ..., 0] (length 100)
