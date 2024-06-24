
## Trees

**Definition:**
A tree is a data structure that consists of nodes, each with some value and pointers to child nodes, which recursively form a tree.

[tree](../assets/tree_definition.png)

**Key Characteristics:**
- The top node is called the root.
- Each node can have zero or more child nodes.
- Nodes without children are called leaf nodes.
- Nodes with children are called internal nodes.

**Common Types of Trees:**

1. **Binary Tree:**
   - A tree in which each node has at most two child nodes.
   - The left child node has a value less than its parent node, and the right child node has a value greater than its parent node.

2. **Perfect Binary Tree:**
   - A binary tree in which all interior nodes have two children and all leaf nodes are at the same depth.

3. **Complete Binary Tree:**
   - A binary tree in which all levels are completely filled except possibly for the last level, which is filled from left to right.

4. **Balanced Binary Tree:**
   - A binary tree in which the height of the left and right subtrees of any node differ by no more than one.

5. **Full Binary Tree:**
   - A binary tree in which every node other than the leaves has two children.

**Common Operations and Complexity Analysis:**

- **Insertion:** O(log n) for balanced trees, O(n) for unbalanced trees.
- **Deletion:** O(log n) for balanced trees, O(n) for unbalanced trees.
- **Searching:** O(log n) for balanced trees, O(n) for unbalanced trees.
- **Traversal:** O(n) for all trees (includes in-order, pre-order, post-order).

**Use Cases:**

- **Binary Search Trees (BST):** Used for quick lookup, insertion, and deletion of items.
- **Heaps:** Used for implementing priority queues.
- **Tries:** Used for efficient retrieval of keys in a dataset of strings.
- **Balanced Trees (e.g., AVL Trees, Red-Black Trees):** Used in databases and file systems to maintain sorted data and allow for efficient insertions, deletions, and lookups.
- **Syntax Trees:** Used in compilers to represent the structure of program code.

