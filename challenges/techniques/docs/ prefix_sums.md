### Pattern 2: Prefix Sums

**Context:**
In coding challenges, the prefix sum is a common pattern used to efficiently solve problems that involve the cumulative sum of elements in an array up to a certain point. 
This technique helps in reducing the time complexity of various problems related to summing subarrays.

**Definition:**
A **prefix sum** is a subarray that contains the first \( k \) elements of an array (where \( 0 \leq k \leq N \)). It represents the cumulative sum of elements from the start of the array up to the \( k \)-th element.

### Example Problem:

**Problem: Find the maximum sum of any subarray of length \( k \).**

**Solution:**
1. Compute the prefix sums of the array.
2. Iterate through the array to find the subarray of length \( k \) with the maximum sum using the prefix sums.

### Python Code Example:

```python
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return "The size of the array is smaller than k"
    
    # Compute the prefix sums
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    
    # Find the maximum sum of a subarray of length k
    max_sum = prefix[k-1]
    for i in range(k, n):
        max_sum = max(max_sum, prefix[i] - prefix[i-k])
    
    return max_sum

# Example usage
arr = [2, 3, 8, -1, 5, 4, 2]
k = 3
print("The maximum sum of a subarray of size {} is {}".format(k, max_sum_subarray(arr, k)))
```

This approach ensures the problem is solved efficiently using the prefix sum pattern.