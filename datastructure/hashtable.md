## Hash Table

**Definition:**
A data structure that provides fast insertion, deletion, and lookup of key/value pairs.

Under the hood, a hash table uses a dynamic array of linked lists to efficiently store key/value pairs. When inserting a key/value pair, a hash function first maps the key, which is typically a string (or any data that can be hashed, depending on the implementation of the hash table), to an integer value and, by extension, to an index in the underlying dynamic array. Then, the value associated with the key is added to the linked list stored at that index in the dynamic array, and a reference to the key is also stored with the value.

Hash tables rely on highly optimized hash functions to minimize the number of collisions that occur when storing values: cases where two keys map to the same index.

**Visual Representation:**
![hash table](../assets/hash-table.png)

In the hash table above, the keys `key2`, `key3`, and `key4` collided by all being hashed to `1`, and the keys `key7` and `key8` collided by both being hashed to `5`.

**Common Operations and Complexity Analysis:**

- **Inserting a key/value pair:** O(1) on average; O(n) in the worst case
- **Removing a key/value pair:** O(1) on average; O(n) in the worst case
- **Looking up a key:** O(1) on average; O(n) in the worst case

The worst-case linear-time operations occur when a hash table experiences a lot of collisions, leading to long linked lists internally, which take O(n) time to traverse.

However, in practice and especially in coding interviews, we typically assume that the hash functions employed by hash tables are so optimized that collisions are extremely rare and constant-time operations are all but guaranteed.

**Use Cases:**

- Efficiently storing and retrieving data using keys
- Implementing associative arrays or dictionaries
- Caching data to improve access times
- Implementing sets, where only keys matter and not values



Here's a list of examples showing how to create, add, update, and delete items in a hash table for various programming languages:

### Python

```python
# Create hash table
hash_table = {}

# Add item
hash_table["key1"] = "value1"

# Update item
hash_table["key1"] = "updated_value1"

# Delete item
del hash_table["key1"]

# Example usage
print(hash_table)
```

### TypeScript

```typescript
// Create hash table
let hashTable: { [key: string]: string } = {};

// Add item
hashTable["key1"] = "value1";

// Update item
hashTable["key1"] = "updated_value1";

// Delete item
delete hashTable["key1"];

// Example usage
console.log(hashTable);
```

### Golang

```go
package main

import "fmt"

func main() {
    // Create hash table
    hashTable := make(map[string]string)

    // Add item
    hashTable["key1"] = "value1"

    // Update item
    hashTable["key1"] = "updated_value1"

    // Delete item
    delete(hashTable, "key1")

    // Example usage
    fmt.Println(hashTable)
}
```

### C++

```cpp
#include <iostream>
#include <unordered_map>

int main() {
    // Create hash table
    std::unordered_map<std::string, std::string> hashTable;

    // Add item
    hashTable["key1"] = "value1";

    // Update item
    hashTable["key1"] = "updated_value1";

    // Delete item
    hashTable.erase("key1");

    // Example usage
    for (const auto& item : hashTable) {
        std::cout << item.first << ": " << item.second << std::endl;
    }

    return 0;
}
```

### Rust

```rust
use std::collections::HashMap;

fn main() {
    // Create hash table
    let mut hash_table = HashMap::new();

    // Add item
    hash_table.insert("key1", "value1");

    // Update item
    hash_table.insert("key1", "updated_value1");

    // Delete item
    hash_table.remove("key1");

    // Example usage
    for (key, value) in &hash_table {
        println!("{}: {}", key, value);
    }
}
```

### Java

```java
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        // Create hash table
        HashMap<String, String> hashTable = new HashMap<>();

        // Add item
        hashTable.put("key1", "value1");

        // Update item
        hashTable.put("key1", "updated_value1");

        // Delete item
        hashTable.remove("key1");

        // Example usage
        for (String key : hashTable.keySet()) {
            System.out.println(key + ": " + hashTable.get(key));
        }
    }
}
```

### Kotlin

```kotlin
fun main() {
    // Create hash table
    val hashTable = mutableMapOf<String, String>()

    // Add item
    hashTable["key1"] = "value1"

    // Update item
    hashTable["key1"] = "updated_value1"

    // Delete item
    hashTable.remove("key1")

    // Example usage
    for ((key, value) in hashTable) {
        println("$key: $value")
    }
}
```




