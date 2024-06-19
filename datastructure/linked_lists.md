## Linked List

### Singly Linked List

**Definition:**

A data structure that consists of nodes, each with some value and a pointer to the next node in the linked list. A linked list node's value and next node are typically stored in `value` and `next` properties, respectively. The first node in a linked list is referred to as the head of the linked list, while the last node in a linked list, whose `next` property points to `null`, is known as the tail of the linked list.

**Visual Representation:**

![Singly linked list](/assets/singly_linked_lists.webp)


**Common Operations and Complexity Analysis:**

- **Accessing the head:** O(1)
- **Accessing the tail:** O(n)
- **Accessing a middle node:** O(n)
- **Inserting / Removing the head:** O(1)
- **Inserting / Removing the tail:** O(n) to access + O(1)
- **Inserting / Removing a middle node:** O(n) to access + O(1)
- **Searching for a value:** O(n)

**Use Cases:**
A singly linked list typically exposes its head to its user for easy access. While finding a node in a singly linked list involves traversing through all of the nodes leading up to the node in question (as opposed to instant access with an array), adding or removing nodes simply involves overwriting `next` pointers (assuming that you have access to the node right before the node that you're adding or removing).

### Doubly Linked List

**Definition:**

Similar to a singly linked list, except that each node in a doubly linked list also has a pointer to the previous node in the linked list. The previous node is typically stored in a `prev` property.

**Visual Representation:**

![Singly linked list](/assets/dll.png)


**Common Operations and Complexity Analysis:**

- **Accessing the head:** O(1)
- **Accessing the tail:** O(1)
- **Accessing a middle node:** O(n)
- **Inserting / Removing the head:** O(1)
- **Inserting / Removing the tail:** O(1)
- **Inserting / Removing a middle node:** O(n) to access + O(1)
- **Searching for a value:** O(n)

**Use Cases:**
While a doubly linked list typically exposes both its head and tail to its user, as opposed to just its head in the case of a singly linked list, it otherwise behaves very similarly to a singly linked list. Just as the `next` property of a doubly linked list's tail points to `null`, so too does the `prev` property of a doubly linked list's head.

### Circular Linked List

**Definition:**

A linked list that has no clear head or tail, because its "tail" points to its "head," effectively forming a closed circle. A circular linked list can be either a singly circular linked list or a doubly circular linked list.

# Examples

Here are examples of how to create, add, update, and delete items in a singly linked list for various programming languages:

### Python

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def update(self, old_value, new_value):
        current = self.head
        while current:
            if current.value == old_value:
                current.value = new_value
                return
            current = current.next

    def delete(self, value):
        current = self.head
        if current and current.value == value:
            self.head = current.next
            return
        prev = None
        while current and current.value != value:
            prev = current
            current = current.next
        if current:
            prev.next = current.next

# Example usage
ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.update(2, 3)
ll.delete(1)
```

### TypeScript

```typescript
class Node {
    value: number;
    next: Node | null = null;

    constructor(value: number) {
        this.value = value;
    }
}

class SinglyLinkedList {
    head: Node | null = null;

    append(value: number): void {
        const newNode = new Node(value);
        if (!this.head) {
            this.head = newNode;
            return;
        }
        let current = this.head;
        while (current.next) {
            current = current.next;
        }
        current.next = newNode;
    }

    update(oldValue: number, newValue: number): void {
        let current = this.head;
        while (current) {
            if (current.value === oldValue) {
                current.value = newValue;
                return;
            }
            current = current.next;
        }
    }

    delete(value: number): void {
        if (this.head && this.head.value === value) {
            this.head = this.head.next;
            return;
        }
        let current = this.head;
        let prev: Node | null = null;
        while (current && current.value !== value) {
            prev = current;
            current = current.next;
        }
        if (current && prev) {
            prev.next = current.next;
        }
    }
}

// Example usage
const ll = new SinglyLinkedList();
ll.append(1);
ll.append(2);
ll.update(2, 3);
ll.delete(1);
```

### Golang

```go
package main

import "fmt"

type Node struct {
    value int
    next  *Node
}

type SinglyLinkedList struct {
    head *Node
}

func (ll *SinglyLinkedList) Append(value int) {
    newNode := &Node{value: value}
    if ll.head == nil {
        ll.head = newNode
        return
    }
    current := ll.head
    for current.next != nil {
        current = current.next
    }
    current.next = newNode
}

func (ll *SinglyLinkedList) Update(oldValue, newValue int) {
    current := ll.head
    for current != nil {
        if current.value == oldValue {
            current.value = newValue
            return
        }
        current = current.next
    }
}

func (ll *SinglyLinkedList) Delete(value int) {
    if ll.head == nil {
        return
    }
    if ll.head.value == value {
        ll.head = ll.head.next
        return
    }
    current := ll.head
    var prev *Node
    for current != nil && current.value != value {
        prev = current
        current = current.next
    }
    if current != nil {
        prev.next = current.next
    }
}

func main() {
    ll := SinglyLinkedList{}
    ll.Append(1)
    ll.Append(2)
    ll.Update(2, 3)
    ll.Delete(1)

    current := ll.head
    for current != nil {
        fmt.Println(current.value)
        current = current.next
    }
}
```

### C++

```cpp
#include <iostream>

class Node {
public:
    int value;
    Node* next;
    Node(int val) : value(val), next(nullptr) {}
};

class SinglyLinkedList {
public:
    Node* head;
    SinglyLinkedList() : head(nullptr) {}

    void append(int value) {
        Node* newNode = new Node(value);
        if (!head) {
            head = newNode;
            return;
        }
        Node* current = head;
        while (current->next) {
            current = current->next;
        }
        current->next = newNode;
    }

    void update(int oldValue, int newValue) {
        Node* current = head;
        while (current) {
            if (current->value == oldValue) {
                current->value = newValue;
                return;
            }
            current = current->next;
        }
    }

    void deleteNode(int value) {
        if (!head) return;
        if (head->value == value) {
            Node* temp = head;
            head = head->next;
            delete temp;
            return;
        }
        Node* current = head;
        Node* prev = nullptr;
        while (current && current->value != value) {
            prev = current;
            current = current->next;
        }
        if (current) {
            prev->next = current->next;
            delete current;
        }
    }
};

int main() {
    SinglyLinkedList ll;
    ll.append(1);
    ll.append(2);
    ll.update(2, 3);
    ll.deleteNode(1);

    Node* current = ll.head;
    while (current) {
        std::cout << current->value << " ";
        current = current->next;
    }

    return 0;
}
```

### Rust

```rust
struct Node {
    value: i32,
    next: Option<Box<Node>>,
}

struct SinglyLinkedList {
    head: Option<Box<Node>>,
}

impl SinglyLinkedList {
    fn new() -> Self {
        Self { head: None }
    }

    fn append(&mut self, value: i32) {
        let new_node = Box::new(Node { value, next: None });
        match &mut self.head {
            Some(mut head) => {
                let mut current = head.as_mut();
                while let Some(ref mut next) = current.next {
                    current = next.as_mut();
                }
                current.next = Some(new_node);
            }
            None => {
                self.head = Some(new_node);
            }
        }
    }

    fn update(&mut self, old_value: i32, new_value: i32) {
        let mut current = self.head.as_mut();
        while let Some(node) = current {
            if node.value == old_value {
                node.value = new_value;
                return;
            }
            current = node.next.as_mut();
        }
    }

    fn delete(&mut self, value: i32) {
        let mut current = self.head.as_mut();
        let mut prev: *mut Box<Node> = std::ptr::null_mut();
        while let Some(node) = current {
            if node.value == value {
                unsafe {
                    if !prev.is_null() {
                        (*prev).next = node.next.take();
                    } else {
                        self.head = node.next.take();
                    }
                }
                return;
            }
            prev = current as *mut _;
            current = node.next.as_mut();
        }
    }
}

fn main() {
    let mut ll = SinglyLinkedList::new();
    ll.append(1);
    ll.append(2);
    ll.update(2, 3);
    ll.delete(1);

    let mut current = ll.head.as_ref();
    while let Some(node) = current {
        println!("{}", node.value);
        current = node.next.as_ref();
    }
}
```

### Java

```java
class Node {
    int value;
    Node next;

    Node(int value) {
        this.value = value;
        this.next = null;
    }
}

class SinglyLinkedList {
    Node head;

    void append(int value) {
        Node newNode = new Node(value);
        if (head == null) {
            head = newNode;
            return;
        }
        Node current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = newNode;
    }

    void update(int oldValue, int newValue) {
        Node current = head;
        while (current != null) {
            if (current.value == oldValue) {
                current.value = newValue;
                return;
            }
            current = current.next;
        }
    }

    void delete(int value) {
        if (head == null) return;
        if (head.value == value) {
            head = head.next;
            return;
        }
        Node current = head;
        Node prev = null;
        while (current != null && current.value != value) {
            prev = current;
            current = current.next;
        }
        if (current != null) {
            prev.next = current.next;
        }
    }

    public static void main(String[] args) {
        SinglyLinkedList ll = new SinglyLinkedList();
        ll.append(1);
        ll.append(2);


        ll.update(2, 3);
        ll.delete(1);

        Node current = ll.head;
        while (current != null) {
            System.out.println(current.value);
            current = current.next;
        }
    }
}
```

### Kotlin

```kotlin
class Node(var value: Int) {
    var next: Node? = null
}

class SinglyLinkedList {
    var head: Node? = null

    fun append(value: Int) {
        val newNode = Node(value)
        if (head == null) {
            head = newNode
            return
        }
        var current = head
        while (current?.next != null) {
            current = current.next
        }
        current?.next = newNode
    }

    fun update(oldValue: Int, newValue: Int) {
        var current = head
        while (current != null) {
            if (current.value == oldValue) {
                current.value = newValue
                return
            }
            current = current.next
        }
    }

    fun delete(value: Int) {
        if (head == null) return
        if (head?.value == value) {
            head = head?.next
            return
        }
        var current = head
        var prev: Node? = null
        while (current != null && current.value != value) {
            prev = current
            current = current.next
        }
        if (current != null) {
            prev?.next = current.next
        }
    }
}

fun main() {
    val ll = SinglyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.update(2, 3)
    ll.delete(1)

    var current = ll.head
    while (current != null) {
        println(current.value)
        current = current.next
    }
}
```


