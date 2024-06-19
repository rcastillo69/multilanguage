# Sliding window pattern

**Pattern 1: Sliding Window** 
refers to a technique used to solve problems involving subarrays (or sublists) of a fixed size within a larger array. 
This technique is useful for optimizing problems that involve calculating sums, averages, or other metrics over all possible subarrays of a given size.

### Step-by-Step Explanation

1. **Initial Setup:**
   - Let's consider an array: `arr = [1, 3, 5, 7, 9, 11, 13]`
   - Window size: 4

2. **Step 1: Calculate the sum of the first window:**
   - Window: `[1, 3, 5, 7]`
   - Sum: \( 1 + 3 + 5 + 7 = 16 \)
   - Store the sum or process it as needed.

3. **Step 2: Slide the window to the right by one position:**
   - Remove the element that is left behind (1) and add the new element that comes into the window (9).
   - New Window: `[3, 5, 7, 9]`
   - New Sum: \( 16 - 1 + 9 = 24 \)
   - Store the sum or process it as needed.

4. **Step 3: Slide the window to the right by one position:**
   - Remove the element that is left behind (3) and add the new element that comes into the window (11).
   - New Window: `[5, 7, 9, 11]`
   - New Sum: \( 24 - 3 + 11 = 32 \)
   - Store the sum or process it as needed.

5. **Step 4: Slide the window to the right by one position:**
   - Remove the element that is left behind (5) and add the new element that comes into the window (13).
   - New Window: `[7, 9, 11, 13]`
   - New Sum: \( 32 - 5 + 13 = 40 \)
   - Store the sum or process it as needed.

### Key Points:
- **Fixed Window Size:** The window size remains constant (in this case, 4).
- **Efficient Calculation:** Instead of recalculating the sum from scratch for each window, we update the sum by subtracting the element that is left behind and adding the new element that comes into the window.
- **Sliding Mechanism:** The window "slides" over the array from left to right by one element at a time.

This technique is powerful because it reduces the time complexity of certain problems from \( O(N \times K) \) to \( O(N) \), where \( N \) is the size of the array and \( K \) is the size of the window.

# Example:

### Challenge Problem: Maximum Sum of a Fixed-Size Subarray

**Description:**
Given an array of integers and an integer `k`, 
find the maximum sum of any subarray (sublist) of size `k`.

**Example:**
- Input: `arr = [2, 1, 5, 1, 3, 2]`, `k = 3`
- Output: `9`
- Explanation: The subarrays of size 3 are `[2, 1, 5]`, `[1, 5, 1]`, `[5, 1, 3]`, `[1, 3, 2]`. 
- The maximum sum is `5 + 1 + 3 = 9`.

### Solution using Sliding Window:

1. **Calculate the sum of the first window of size `k`:**
    - Initial sum: `2 + 1 + 5 = 8`

2. **Slide the window across the array:**
    - For each step, subtract the first element of the current window and add the next element in the sequence.

3. **Update the maximum sum if the sum of the new window is greater:**

### Python Code:

```python
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return "The size of the array is smaller than k"

    # Calculate the sum of the first window
    max_sum = sum(arr[:k])
    window_sum = max_sum

    # Slide the window across the array
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example usage
arr = [2, 1, 5, 1, 3, 2]
k = 3
print("The maximum sum of a subarray of size {} is {}".format(k, max_sum_subarray(arr, k)))
```

### Explanation of the Code:

1. **Initial Sum:** Calculate the sum of the first window of size `k`.
2. **Slide the Window:** Use a loop to move the window to the right, one element at a time.
    - Subtract the first element of the current window (`arr[i]`).
    - Add the new element entering the window (`arr[i + k]`).
3. **Update the Maximum Sum:** Compare the sum of the current window with the recorded maximum sum and update if it is greater.

This technique ensures that the problem is solved in linear time \( O(N) \), which is much more efficient than recalculating the sum from scratch for each window.
