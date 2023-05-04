# multilanguage
## Objectives

This repository summarizes the relevant aspects of the following languages:
# Server oriented
- Rust
- Go
- Zig

# Functional oriented
- Clojure
- Elixir / Erlang
- Racket

# Script oriented
- Typescript
- Python
- Julia

# Mobile oriented
- Kotlin
- Dart
- Swift

The topics to be reviewed in each language are as follows

## Basic Features
* Program outputs and Comments
    * Main
    * Comments
      * Single Line
      * Multiple Lines
    * Console Ouput
    * Compile / Debug
    * Output Console
        * Format output   

## Variables & System Types

### System data types

#### Primitive types & Variables, values
* Constant
* Numbers
    * Integer 32/64 bits
        * Signed
        * Unsigned
* Floating Point 32/64
* Boolean
* Date, Time & Datetime
* String
  * Literal
  * String object
  * Concatenation
* Char

* Declaring Variables
    * Explicit
    * Implicit
* Group of declarations
* Multiple declarations inline
* Check Type
* Casting Data Types
* Mutability / Immutability

#### Special types
* Null value
* Pointers & Address



#### Operators

* Arithmetic operators: used to perform basic mathematical operations, such as addition (+), subtraction (-), multiplication (*), division (/), modulus or remainder (%), increment (++) and decrement (--).

* Assignment operators: used to assign values to variables, such as the assignment operator (=) and other compound assignment operators such as +=, -=, *=, /=, %=.

* Comparison operators: used to compare values, such as equality (==), inequality (!=), greater than (>), less than (<), greater than or equal to (>=) and less than or equal to (<=).

* Logical operators: used to perform Boolean operations, such as the logical operator and (&&), the logical operator or (||), and the logical negation operator (!).
Bitwise operators: used to perform bitwise operations, such as the left shift operator (<<), the right shift operator (>>), the bitwise and operator (&), the bitwise or operator (|), and the bitwise negation operator (~).

* Concatenation operators: used to concatenate character strings or values, such as the concatenation operator (+).

* Conditional operators: used to assign values to a variable based on a condition, such as the ternary conditional operator (?).

#### Composite types
* Characters & Strings
    * Concatenation
    * Operations
* Enum
  * Operations
* Structure or Record
  * Operations
* Slice
  * Operations
* Array
  * Operations
  * Vector
    * Operations
  *  Multi-dimensional arrays
     *  Operations
* Tuples
  * Operations
* Dictionaries or Maps
  * Operations
* Lists
* Sets




## Flow
### Decision
    * Simple
    * Nested
    * Multiple
### Loop
    * Simple
        * While
        * Loop
        * For
    * Continue & Escaping

## Functions
    * Declaration
    * Function parameters and arguments
    * Function return values
    * Recursion

## Error Handling
### I. Introduction to Error Handling
   * A. What is Error Handling?
   * B. Importance of Error Handling in programming
   * C. Types of errors: compile-time, runtime, and logical errors

### II. Basic Error Handling Techniques
   * A. Return values and error codes
   * B. Error handling functions and methods
   * C. Assertions

### III. Exceptions
   * A. What are exceptions?
   * B. Exception hierarchy and built-in exceptions
   * C. Creating custom exceptions

### IV. Try-Catch-Finally Blocks
   * A. The try block: capturing exceptions
   * B. The catch block: handling exceptions
       1. Catching specific exceptions
       2. Catching multiple exceptions
   * C. The finally block: executing code regardless of exception occurrence
   * D. Nested try-catch-finally blocks

### V. Raising and Throwing Exceptions
   * A. Raising exceptions
   * B. Throwing exceptions

### VI. Resource Management and Cleanup
   * A. Proper resource allocation and deallocation
   * B. Using with statements (context managers) for resource management

## VII. Best Practices for Error Handling
   * A. Defensive programming
   * B. Handling exceptions at the appropriate level
   * C. Providing meaningful error messages and logging
   * D. Failing fast and early
   * E. Testing and debugging strategies

## Modules & Library

## Standard Libray

## Memory Management
## 1. Introduction to Memory Management
- 1.1. What is memory management?
- 1.2. Importance of memory management
- 1.3. Memory hierarchy and types
- 1.4. Stack vs. heap memory

## 2. Basic Memory Management Concepts
- 2.1. Memory allocation
- 2.2. Memory deallocation
- 2.3. Memory leaks
- 2.4. Memory fragmentation
- 2.5. Garbage collection

## 3. Manual Memory Management
- 3.1. Memory allocation and deallocation functions
- 3.2. Pointers and pointer arithmetic
- 3.3. Common pitfalls and best practices

## 4. Automatic Memory Management
- 4.1. Garbage collection algorithms
- 4.2. Reference counting
- 4.3. Smart pointers

## 5. Rust-Specific Memory Management
- 5.1. Ownership
  - 5.1.1. What is ownership?
  - 5.1.2. Rules of ownership
  - 5.1.3. Ownership and functions
- 5.2. Borrowing
  - 5.2.1. What is borrowing?
  - 5.2.2. Mutable and immutable references
  - 5.2.3. Borrowing rules and restrictions
- 5.3. Lifetimes
  - 5.3.1. What are lifetimes?
  - 5.3.2. Lifetime annotations
  - 5.3.3. Lifetime elision

## 6. Advanced Memory Management Techniques
- 6.1. Memory pools
- 6.2. Custom allocators
- 6.3. Cache-aware and cache-oblivious algorithms
- 6.4. Memory optimization techniques

## 7. Memory Profiling and Debugging
- 7.1. Memory profiling tools
- 7.2. Detecting memory leaks
- 7.3. Debugging memory-related issues

## 8. Real-World Memory Management Examples
- 8.1. Memory management in operating systems
- 8.2. Memory management in databases
- 8.3. Memory management in game engines

## 9. Practical Projects and Exercises
- 9.1. Implementing a simple memory allocator
- 9.2. Developing a memory-efficient data structure
- 9.3. Optimizing memory usage in a real-world application


## Oriented Program paradigm 
* Defining classes
  * Creating objects
  * Instance variables and methods
* Inheritance
  * Base and derived classes
  * Method overriding
  * Multiple inheritance
* Polymorphism
  * Method overloading
  * Operator overloading
* Encapsulation
  * Access modifiers
  * Properties and methods
* Abstract classes and interfaces
* Design patterns

## Functional paradigm 
### I. Introduction to Functional Programming
   * A. What is functional programming?
   * B. Functional vs. imperative programming
   * C. Advantages and disadvantages of functional programming
   * D. Functional programming languages (Haskell, Lisp, Scala, etc.)

### II. Core Concepts of Functional Programming
   * A. Pure Functions
       1. Immutability
       2. No side effects
       3. Referential transparency
   * B. First-class Functions
       1. Functions as arguments
       2. Functions as return values
       3. Functions as data structures
   * C. Higher-order Functions
       1. Map
       2. Filter
       3. Reduce (or Fold)
   * D. Recursion
       1. Recursive functions
       2. Tail recursion
       3. Accumulators

### III. Functional Programming Techniques
   * A. Lambda Functions (or Anonymous Functions)
   * B. Function Composition
   * C. Currying and Partial Application
   * D. Lazy Evaluation
   * E. Monads
   * F. Pattern Matching
   * G. Algebraic Data Types

### IV. Functional Data Structures
   * A. Immutable Data Structures
       1. Immutable lists
       2. Immutable sets
       3. Immutable maps (or dictionaries)
   * B. Persistent Data Structures
       1. Persistent arrays
       2. Persistent trees
## Concurrency, Multithreading, and Parallelism

### I. Introduction to Concurrency and Parallelism
   * A. What is Concurrency?
   * B. What is Parallelism?
   * C. Importance and benefits of Concurrency and Parallelism
   * D. Concurrency vs. Parallelism

### II. Multithreading
   * A. Introduction to Threads
       1. What is a Thread?
       2. Threads vs. Processes
   * B. Creating Threads
       1. Thread creation in different programming languages
       2. Thread lifecycle
   * C. Thread Synchronization
       1. Race conditions
       2. Critical sections
       3. Mutexes and Locks
       4. Semaphores
       5. Monitors and Condition Variables
   * D. Deadlocks
       1. Deadlock causes and detection
       2. Deadlock prevention
       3. Deadlock avoidance

### III. Parallel Programming
   * A. Parallel Programming Models
       1. Data parallelism
       2. Task parallelism
       3. Pipeline parallelism
   * B. Parallel Programming Constructs
       1. Fork-join
       2. MapReduce
       3. Parallel loops
       4. Parallel aggregations
   * C. Load Balancing
       1. Static vs. dynamic load balancing
       2. Work stealing

### IV. Concurrent Data Structures
   * A. Introduction to Concurrent Data Structures
   * B. Lock-based Data Structures
   * C. Lock-free Data Structures
   * D. Wait-free Data Structures

### V. Asynchronous Programming
   * A. Asynchronous vs. Synchronous Programming
   * B. Callbacks
   * C. Promises and Futures
   * D. Async/Await
   * E. Event-driven Programming

### VI. Message Passing and Distributed Systems
   * A. Message Passing Interface (MPI)
   * B. Actor Model
   * C. Remote Procedure Calls (RPC)
   * D. Publish-Subscribe Pattern

### VII. Hardware and Architectures for Parallelism
   * A. Multicore Processors
   * B. Graphics Processing Units (GPUs)
       1. CUDA
       2. OpenCL
   * C. Clusters and Supercomputers

### VIII. Performance Analysis and Optimization
   * A. Performance Metrics
   * B. Amdahl's Law and Gustafson's Law
   * C. Profiling and Benchmarking
   * D. Parallel Performance Tuning

### IX. Real-world Applications
   * A. High-Performance Computing (HPC)
   * B. Scientific Computing
   * C. Big Data Processing
   * D. Web Servers and Databases


## File I/O
### I. Introduction to File I/O
   * A. What is File I/O?
   * B. Importance of File I/O in programming
   * C. Types of files: text and binary
   * D. File encoding and character sets

### II. Reading and Writing Files
   * A. Opening and closing files
       1. File modes (read, write, append)
       2. Error handling and exceptions
   * B. Reading from files
       1. Reading the entire file
       2. Reading a specific number of bytes or characters
       3. Reading line by line
       4. File iterators
   * C. Writing to files
       1. Writing data to a file
       2. Writing line by line
       3. Truncating and overwriting files

### III. File Manipulation
   * A. File metadata
       1. File size
       2. File permissions
       3. File timestamps
   * B. File and directory operations
       1. Renaming and moving files
       2. Deleting files
       3. Creating directories
       4. Listing directory contents
       5. Removing directories

### IV. Working with Text Files
   * A. String manipulation and formatting
   * B. Regular expressions
   * C. Parsing structured text formats
       1. CSV
       2. JSON
       3. XML

### V. Working with Binary Files
   * A. Binary file formats
   * B. Reading and writing binary data
   * C. Endianness
   * D. Binary file manipulation

### VI. Serialization and Deserialization
   * A. What is serialization and deserialization?
   * B. Serialization formats
       1. Binary serialization
       2. JSON serialization
       3. XML serialization
   * C. Custom serialization and deserialization methods

### VII. Memory-Mapped Files
   * A. Introduction to memory-mapped files
   * B. Advantages and use cases
   * C. Creating and accessing memory-mapped files

### VIII. File I/O Performance
   * A. Buffering and caching
   * B. Asynchronous File I/O
   * C. File I/O performance tuning and best practices
## Data structure

### Introduction to Data Structures
* Importance of data structures in programming
* Types of data structures
* Time and space complexity
* Choosing the right data structure for a problem

### Linear Data Structures
* Arrays
  * Fixed-size arrays
  * Dynamic arrays
  * Multi-dimensional arrays
  * Array operations and algorithms
* Linked Lists
  * Singly-linked lists
  * Doubly-linked lists
  * Circular linked lists
  * Linked list operations and algorithms
* Stacks
  * Array-based stacks
  * Linked list-based stacks
  * Stack operations and use cases
* Queues
  * Array-based queues
  * Linked list-based queues
  * Double-ended queues (Deque)
  * Priority queues
  * Queue operations and use cases

### Non-Linear Data Structures

* Trees
  * Binary trees
  * Binary search trees
  * Balanced trees (AVL, Red-Black)
* Heaps
  * Trie
  * Tree operations and traversal algorithms
* Graphs
  * Directed graphs
  * Undirected graphs
  * Weighted graphs
  * Graph representations (adjacency matrix, adjacency list)
  * Graph operations and traversal algorithms (DFS, BFS)

### Hash-based Data Structures

* Hash Tables
  * Hash functions
  * Collision resolution (chaining, open addressing)
  * Load factor and resizing
  * Hash table operations and use cases
* Bloom Filters
  * Probabilistic data structures
  * False positives and false negatives
  * Use cases for Bloom filters

### Advanced Data Structures

* Spatial data structures
  * Quadtrees
  * Octrees
  * k-d trees
* Temporal data structures
  * Persistent data structures
  * Retroactive data structures
* Concurrent data structures
  * Lock-free data structures
  * Wait-free data structures

### Data Structure Analysis and Design
* Analyzing data structure performance
* Best-case, worst-case, and average-case analysis
* Big O, Big Theta, and Big Omega notation
* Designing custom data structures for specific problems
* Trade-offs between data structure choice and performance

## Networking
## Fundamentals of Networking
- OSI Model
  - Physical Layer
  - Data Link Layer
  - Network Layer
  - Transport Layer
  - Session Layer
  - Presentation Layer
  - Application Layer
- IP Addressing
  - IPv4
  - IPv6
- Domain Name System (DNS)
- Network Address Translation (NAT)

## TCP/IP Protocol Suite
- TCP (Transmission Control Protocol)
- UDP (User Datagram Protocol)
- HTTP (Hypertext Transfer Protocol)
  - HTTP/1.1
  - HTTP/2
  - HTTPS (Secure HTTP)
- FTP (File Transfer Protocol)
- SMTP (Simple Mail Transfer Protocol)

## RESTful Services
- REST (Representational State Transfer) Principles
- CRUD Operations
  - Create
  - Read
  - Update
  - Delete
- JSON (JavaScript Object Notation)
- XML (eXtensible Markup Language)
- API Design Best Practices
- API Documentation and Versioning

## WebSockets
- WebSocket Protocol
- Real-time Communication
- WebSocket Events
  - Connection
  - Disconnection
  - Message
- Broadcast and Unicast Messages
- WebSocket Security

## Sockets
- Socket Programming
- TCP Sockets
- UDP Sockets
- Multithreading in Socket Programming
- Multiplexing and Select
- Non-blocking Sockets

## Other Relevant Networking Services
- MQTT (Message Queue Telemetry Transport)
- gRPC (gRPC Remote Procedure Call)
- SOAP (Simple Object Access Protocol)

## Security in Networking Services
- Authentication
  - Basic Authentication
  - Token-based Authentication
  - OAuth 2.0
- Authorization
- Data Encryption
  - SSL/TLS (Secure Sockets Layer/Transport Layer Security)
  - HTTPS
- CORS (Cross-Origin Resource Sharing)

# Reactive Programming: From Zero to Expert

## 1. Introduction to Reactive Programming
- 1.1. What is reactive programming?
- 1.2. Benefits of reactive programming
- 1.3. Comparison to imperative and functional programming

## 2. Core Concepts of Reactive Programming
- 2.1. Data streams
- 2.2. Observables and observers
- 2.3. Subscriptions
- 2.4. Subjects

## 3. Functional Programming Basics
- 3.1. Pure functions
- 3.2. Higher-order functions
- 3.3. Immutability
- 3.4. Functional composition

## 4. Reactive Programming Operators
- 4.1. Creating observables
- 4.2. Transforming observables
- 4.3. Filtering observables
- 4.4. Combining observables
- 4.5. Error handling and recovery

## 5. Reactive Programming in Practice
- 5.1. Handling user input
- 5.2. Reactive data fetching and state management
- 5.3. Real-time updates and live data
- 5.4. Backpressure and buffering strategies

## 6. Reactive Programming Libraries and Frameworks
- 6.1. Overview of popular libraries and frameworks
- 6.2. Reactive Extensions (Rx)
- 6.3. Reactive Streams implementations (e.g., Reactor, Akka Streams)
- 6.4. Language-specific reactive libraries (e.g., RxJava, RxJS, RxDart)

## 7. Reactive Architectures and Patterns
- 7.1. Event-driven architecture
- 7.2. Microservices and reactive systems
- 7.3. Command Query Responsibility Segregation (CQRS) and Event Sourcing
- 7.4. Reactive design patterns

## 8. Testing Reactive Applications
- 8.1. Unit testing observables and operators
- 8.2. Integration testing reactive components
- 8.3. End-to-end testing reactive applications
- 8.4. Debugging and troubleshooting

## 9. Performance and Optimization
- 9.1. Measuring performance in reactive applications
- 9.2. Optimizing data streams and operators
- 9.3. Concurrency and parallelism in reactive systems
- 9.4. Resource management and best practices

## 10. Practical Projects and Exercises
- 10.1. Building a simple reactive application
- 10.2. Implementing custom reactive operators
- 10.3. Refactoring an existing application to use reactive programming

