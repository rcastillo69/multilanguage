### Pattern: Two Pointers

**Description:**
The two pointers technique involves using two indices (or pointers) to iterate through an array from different ends 
or based on specific conditions. 
This approach is particularly effective for reducing the complexity of certain problems, 
especially when dealing with sorted arrays or situations where you need to compare elements 
from different parts of the array.

**Use Cases:**
1. **Finding pairs in an array that sum up to a target:**
    - Given a sorted array and a target sum, find all pairs of elements that add up to the target sum.

2. **Removing duplicates from a sorted array:**
    - Given a sorted array, remove duplicates in-place such that each element appears only once and return the new length.

3. **Container with most water:**
    - Given an array representing the height of lines on the x-axis, find two lines that together with the x-axis form a container that holds the most water.

### Example 1: Finding Pairs in an Array that Sum up to a Target

**Problem:**
Given a sorted array of integers and a target sum, find all pairs of elements that add up to the target sum.

**Solution:**

1. Initialize two pointers, `left` at the start of the array and `right` at the end of the array.
2. Move the pointers towards each other based on the sum of the elements at these pointers.
3. If the sum is equal to the target, record the pair.
4. If the sum is less than the target, move the `left` pointer to the right.
5. If the sum is greater than the target, move the `right` pointer to the left.

**Code Example:**

```python
def find_pairs_with_sum(arr, target):
    left, right = 0, len(arr) - 1
    pairs = []

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return pairs

# Example usage 
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
print("Pairs with sum", target, ":", find_pairs_with_sum(arr, target))
```

**Output:**
```
Pairs with sum 10 : [(1, 9), (2, 8), (3, 7), (4, 6)]
```

### Example 2: Removing Duplicates from a Sorted Array

**Problem:**
Given a sorted array, remove the duplicates in-place such that each element appears only once and return the new length.

**Solution:**

1. Use two pointers: `write_index` to track the position where the next unique element should be written, and `i` to iterate through the array.
2. Initialize `write_index` to 1 (the position of the second element).
3. Iterate through the array starting from the second element (`i = 1`).
4. If the current element is different from the previous element, write it at the `write_index` and increment `write_index`.
5. Continue until the end of the array.

**Code Example:**

```python
def remove_duplicates(arr):
    if not arr:
        return 0
    
    write_index = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[write_index] = arr[i]
            write_index += 1
    
    return write_index

# Example usage
arr = [1, 1, 2, 2, 3, 4, 4, 5]
new_length = remove_duplicates(arr)
print("Array after removing duplicates:", arr[:new_length])
```

**Output:**
```
Array after removing duplicates: [1, 2, 3, 4, 5]
```

### Summary

The two pointers technique is a powerful tool for solving various problems involving arrays. It helps reduce complexity by enabling simultaneous traversal and comparison of elements from different parts of the array. This technique is particularly useful for problems such as finding pairs with a specific sum, removing duplicates, and solving the container with most water problem.