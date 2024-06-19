### Pattern 3: Array-based Histogram

**Context:**
In coding challenges, the array-based histogram is a useful pattern for solving problems that require counting occurrences of elements within an array. This technique leverages an array to keep track of counts, making it efficient for small value ranges.

**Definition:**
A histogram is a mapping from "values" to "counts". An array-based histogram is an array where the indices represent the values, and the elements at these indices represent the counts of these values.

### Key Points:
- **Array-based Histogram:** Use an array with indices ranging from 0 to `MAX_VAL` (maximum possible value in the array).
- **Histogram[x]:** Contains the number of occurrences of x (where \( 0 \leq x \leq \text{MAX_VAL} \)).

### Example Problem: Equalize the Array

**Problem Statement:**
Given an array of integers, determine the minimum number of elements to delete to leave only elements of equal value.

**Example:**
- Input: `arr = [1, 2, 2, 3]`
- Output: `2`
- Explanation: Delete elements `1` and `3` to leave `[2, 2]`.

**Constraints:**
- \( 1 \leq n \leq 100 \)
- \( 1 \leq \text{arr}[i] \leq 100 \)

### Solution Using Histogram:

1. **Create a Histogram:**
    - Count occurrences of each element in the array using an array-based histogram.

2. **Find the Most Common Element:**
    - Determine the element with the highest count.

3. **Calculate Minimum Deletions:**
    - The minimum number of deletions is the total number of elements minus the count of the most common element.

### Python Code Example:

```python
def equalizeArray(arr):
    MAX_VAL = 100
    histogram = [0] * (MAX_VAL + 1)

    # Populate the histogram
    for x in arr:
        histogram[x] += 1

    # Find the maximum count in the histogram
    max_count = max(histogram)

    # The minimum deletions required
    min_deletions = len(arr) - max_count

    return min_deletions

# Example usage
arr = [1, 2, 2, 3]
print("The minimum number of deletions is", equalizeArray(arr))
```

### Explanation of the Code:

1. **Histogram Creation:** Initialize a histogram array with zeros, then iterate through the input array to count the occurrences of each element.
2. **Finding Maximum Count:** Use the `max` function to find the highest count in the histogram.
3. **Calculating Deletions:** Subtract the highest count from the total number of elements in the array to get the minimum deletions required.

This approach ensures an efficient solution, leveraging the array-based histogram pattern to quickly count and compare element frequencies.