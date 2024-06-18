# Complexity analysis


**Complexity Analysis** is the study of how the computational resources required by an algorithm scale with the size of the input. 
The primary resources considered in complexity analysis are time and space:

1. **Time Complexity**: 
   This refers to the amount of time an algorithm takes to complete as a function of the size of the input. It helps in understanding the efficiency of an algorithm in terms of execution time.

2. **Space Complexity**: 
   This refers to the amount of memory space an algorithm uses as a function of the size of the input. It helps in understanding the efficiency of an algorithm in terms of memory usage.

![Types of Complexity](/assets/types-complexity-analysis.png)

**Key Concepts in Complexity Analysis**:

1. **Big O Notation (O)**: Represents the upper bound of the time complexity, showing the worst-case scenario.

2. **Omega Notation (Ω)**: Represents the lower bound of the time complexity, showing the best-case scenario.

3. **Theta Notation (Θ)**: Represents the exact bound of the time complexity, showing both the upper and lower bounds.

4. **Asymptotic Analysis**: Involves studying the behavior of algorithms as the input size approaches infinity.

5. **Worst-Case Analysis**: Determines the maximum time or space an algorithm can take for the worst possible input of a given size.

6. **Best-Case Analysis**: Determines the minimum time or space an algorithm can take for the best possible input of a given size.

7. **Average-Case Analysis**: Determines the expected time or space an algorithm will take, averaged over all possible inputs.

8. **Amortized Analysis**: Analyzes the average time per operation over a worst-case sequence of operations, smoothing out the occasional costly operations over many inexpensive ones.

Understanding complexity analysis helps in selecting the most appropriate algorithm for a given problem by comparing the efficiency and scalability of different algorithms.

## Big O Notation

One way to express time complexity is by using Big O notation. 
This notation describes the upper bound of an algorithm’s time complexity, 
or the worst-case scenario. 
For example, if an algorithm has a time complexity of O(n), where n is the size of the input data, 
it means that the algorithm will take at most n operations to complete.

## Calculation of Time Complexity

Calculating time complexity involves analysing the algorithm’s steps and their efficiency. 
For example, if an algorithm has a loop that iterates through n elements 
and performs a constant-time operation on each element, 
its time complexity is O(n)
![Rates](/assets/big-O-notation-rates.webp)

![Rates](/assets/calculating-time-complexity-big-O-notation.webp)

## Understanding Space Complexity

In addition to time complexity, space complexity is another important consideration for optimising code performance. 
Space complexity refers to the amount of memory an algorithm uses to complete its task.

Space complexity refers to the amount of memory an algorithm uses in its worst-case scenario. 
This includes the memory used by the algorithm’s variables, 
data structures, and auxiliary space.

## Calculation of Space Complexity

Calculating space complexity involves analysing an algorithm’s memory usage. 
We count the space used by the algorithm’s variables, data structures, and auxiliary space. 
Auxiliary space refers to any additional space used by the algorithm, 
such as the space used by recursive function calls.

Here are some examples of different space complexities:

- O(1): Constant space complexity. An algorithm that uses a fixed amount of memory, regardless of the input size, has O(1) space complexity.
- O(n): Linear space complexity. An algorithm that uses memory proportional to the input size, such as an array or a linked list, has O(n) space complexity.
- O(n²): Quadratic space complexity. An algorithm that uses memory proportional to the square of the input size, such as a matrix or a nested data structure, has O(n²) space complexity.

![](/assets/DSA-complexity-analysis.webp)