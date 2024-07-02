def countingSort(arr):
    freq = [0] * 100
   
    for num in arr:
        freq[num] += 1
    
    sorted_arr = []
    for number, count in enumerate(freq):
        sorted_arr.extend([number] * count)
    
    return sorted_arr

# Example usage
arr = [1, 1, 3, 2, 1]
print(countingSort(arr))  # Output: [1, 1, 1, 2, 3]
