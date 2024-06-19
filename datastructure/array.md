## Array

**Definition:**
A linear collection of data values that are accessible at numbered indices, starting at index 0.

**Common Operations and Complexity Analysis:**

- **Accessing a value at a given index:** O(1)
- **Updating a value at a given index:** O(1)
- **Inserting a value at the beginning:** O(n)
- **Inserting a value in the middle:** O(n)
- **Inserting a value at the end:**
  - amortized O(1) when dealing with a *dynamic array*
  - O(n) when dealing with a *static array*
- **Removing a value at the beginning:** O(n)
- **Removing a value in the middle:** O(n)
- **Removing a value at the end:** O(1)
- **Copying the array:** O(n)

**Use Cases:**

- **Static Array:** A static array is an implementation of an array that allocates a fixed amount of memory to be used for storing the array's values. Appending values to the array therefore involves copying the entire array and allocating new memory for it, accounting for the extra space needed for the newly appended value. This is a linear-time operation.
  
- **Dynamic Array:** A dynamic array is an implementation of an array that preemptively allocates double the amount of memory needed to store the array's values. Appending values to the array is a constant-time operation until the allocated memory is filled up, at which point the array is copied and double the memory is once again allocated for it. This implementation leads to an amortized constant-time insertion-at-end operation.

**Implementation:**

A lot of popular programming languages like JavaScript and Python implement arrays as dynamic arrays.

## Examples

Here's a list of examples showing how to create, add, update, and delete items in an array for various programming languages:

### Python

```python
# Create array
arr = [1, 2, 3]

# Add item
arr.append(4)

# Update item
arr[1] = 5

# Delete item
del arr[2]
```

### TypeScript

```typescript
// Create array
let arr: number[] = [1, 2, 3];

// Add item
arr.push(4);

// Update item
arr[1] = 5;

// Delete item
arr.splice(2, 1);
```

### Golang

```go
package main

import "fmt"

func main() {
    // Create array
    arr := []int{1, 2, 3}

    // Add item
    arr = append(arr, 4)

    // Update item
    arr[1] = 5

    // Delete item
    arr = append(arr[:2], arr[3:]...)

    fmt.Println(arr)
}
```

### C++

```cpp
#include <iostream>
#include <vector>

int main() {
    // Create array
    std::vector<int> arr = {1, 2, 3};

    // Add item
    arr.push_back(4);

    // Update item
    arr[1] = 5;

    // Delete item
    arr.erase(arr.begin() + 2);

    for (int i : arr)
        std::cout << i << " ";

    return 0;
}
```

### Rust

```rust
fn main() {
    // Create array
    let mut arr = vec![1, 2, 3];

    // Add item
    arr.push(4);

    // Update item
    arr[1] = 5;

    // Delete item
    arr.remove(2);

    for i in arr.iter() {
        println!("{}", i);
    }
}
```

### Java

```java
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // Create array
        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(1);
        arr.add(2);
        arr.add(3);

        // Add item
        arr.add(4);

        // Update item
        arr.set(1, 5);

        // Delete item
        arr.remove(2);

        for (int i : arr) {
            System.out.println(i);
        }
    }
}
```

### Kotlin

```kotlin
fun main() {
    // Create array
    val arr = mutableListOf(1, 2, 3)

    // Add item
    arr.add(4)

    // Update item
    arr[1] = 5

    // Delete item
    arr.removeAt(2)

    for (i in arr) {
        println(i)
    }
}
```

These examples demonstrate basic array operations such as creating, adding, updating, and deleting items in various programming languages.