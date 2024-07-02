## Problem 013

### Problem Statement
The median of a list of numbers is essentially its middle element after sorting. The same number of elements occur after it as before. Given a list of numbers with an odd number of elements, find the median.

### Example
Given the array `arr = [5, 3, 1, 2, 4]`, the sorted array `arr' = [1, 2, 3, 4, 5]`. The middle element and the median is `3`.

### Function Description
Complete the `findMedian` function in the editor below.

### Input Format
- The first line contains an integer `n`, the size of `arr`.
- The second line contains `n` space-separated integers `arr[i]`.

### Constraints
- \( 1 \leq n \leq 1000001 \)
- `n` is odd
- \( -10000 \leq arr[i] \leq 10000 \)

### Sample Input
```
7
0 1 2 4 6 5 3
```

### Sample Output
```
3
```

### Explanation
The sorted `arr = [0, 1, 2, 3, 4, 5, 6]`. Its middle element is at `arr[3] = 3`.

