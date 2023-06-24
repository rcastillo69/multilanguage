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
    * Console Output
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
  * multiline
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

#### Composite types
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






## Functions
    * Declaration
    * Function parameters and arguments
    * Function return values
    * Recursion

## Error Handling
### Introduction to Error Handling
   * What is Error Handling?
   * Importance of Error Handling in programming
   * Types of errors: compile-time, runtime, and logical errors

### Basic Error Handling Techniques
   * Return values and error codes
   * Error handling functions and methods
   * Assertions

### Exceptions
   * What are exceptions?
   * Exception hierarchy and built-in exceptions
   * Creating custom exceptions

### Try-Catch-Finally Blocks
   * The try block: capturing exceptions
   * The catch block: handling exceptions
       Catching specific exceptions
       Catching multiple exceptions
   * The finally block: executing code regardless of exception occurrence
   * Nested try-catch-finally blocks

### Raising and Throwing Exceptions
   * Raising exceptions
   * Throwing exceptions

### Resource Management and Cleanup
   * Proper resource allocation and deallocation
   * Using with statements (context managers) for resource management

## Best Practices for Error Handling
   * Defensive programming
   * Handling exceptions at the appropriate level
   * Providing meaningful error messages and logging
   * Failing fast and early
   * Testing and debugging strategies

## Modules & Library

## Standard Libray

## Memory Management
## Introduction to Memory Management
- What is memory management?
- Importance of memory management
- Memory hierarchy and types
- Stack vs. heap memory

## Basic Memory Management Concepts
- Memory allocation
- Memory deallocation
- Memory leaks
- Memory fragmentation
- Garbage collection

## Manual Memory Management
- Memory allocation and deallocation functions
- Pointers and pointer arithmetic
- Common pitfalls and best practices

## Automatic Memory Management
- Garbage collection algorithms
- Reference counting
- Smart pointers

## Rust-Specific Memory Management
- Ownership
  - What is ownership?
  - Rules of ownership
  - Ownership and functions
- Borrowing
  - What is borrowing?
  - Mutable and immutable references
  - Borrowing rules and restrictions
-  Lifetimes
  - What are lifetimes?
  - Lifetime annotations
  - Lifetime elision

## Advanced Memory Management Techniques
- Memory pools
- Custom allocators
- Cache-aware and cache-oblivious algorithms
- Memory optimization techniques

## Memory Profiling and Debugging
- Memory profiling tools
- Detecting memory leaks
- Debugging memory-related issues

## Real-World Memory Management Examples
- Memory management in operating systems
- Memory management in databases
- Memory management in game engines

## Practical Projects and Exercises
- Implementing a simple memory allocator
- Developing a memory-efficient data structure
- Optimizing memory usage in a real-world application


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
### Introduction to Functional Programming
   * What is functional programming?
   * Functional vs. imperative programming
   * Advantages and disadvantages of functional programming
   * Functional programming languages (Haskell, Lisp, Scala, etc.)

### Core Concepts of Functional Programming
   * Pure Functions
      Immutability
      No side effects
      Referential transparency
   * First-class Functions
       Functions as arguments
       Functions as return values
       Functions as data structures
   * Higher-order Functions
       Map
       Filter
       Reduce (or Fold)
   * Recursion
       Recursive functions
       Tail recursion
       Accumulators

### Functional Programming Techniques
   * Lambda Functions (or Anonymous Functions)
   * Function Composition
   * Currying and Partial Application
   * Lazy Evaluation
   * Monads
   * Pattern Matching
   * Algebraic Data Types

### Functional Data Structures
   * Immutable Data Structures
       Immutable lists
       Immutable sets
       Immutable maps (or dictionaries)
   * Persistent Data Structures
       Persistent arrays
       Persistent trees
## Concurrency, Multithreading, and Parallelism

### Introduction to Concurrency and Parallelism
   * What is Concurrency?
   * What is Parallelism?
   * Importance and benefits of Concurrency and Parallelism
   * Concurrency vs. Parallelism

### Multithreading
   * Introduction to Threads
       What is a Thread?
       Threads vs. Processes
   * Creating Threads
       Thread creation in different programming languages
       Thread lifecycle
   * Thread Synchronization
       Race conditions
       Critical sections
       Mutexes and Locks
       Semaphores
       Monitors and Condition Variables
   * Deadlocks
       Deadlock causes and detection
       Deadlock prevention
       Deadlock avoidance

### Parallel Programming
   * Parallel Programming Models
       Data parallelism
       Task parallelism
       Pipeline parallelism
   * Parallel Programming Constructs
       Fork-join
       MapReduce
       Parallel loops
       Parallel aggregations
   * Load Balancing
       Static vs. dynamic load balancing
       Work stealing

### Concurrent Data Structures
   * Introduction to Concurrent Data Structures
   * Lock-based Data Structures
   * Lock-free Data Structures
   * Wait-free Data Structures

### Asynchronous Programming
   * Asynchronous vs. Synchronous Programming
   * Callbacks
   * Promises and Futures
   * Async/Await
   * Event-driven Programming

### Message Passing and Distributed Systems
   * Message Passing Interface (MPI)
   * Actor Model
   * Remote Procedure Calls (RPC)
   * Publish-Subscribe Pattern

### Hardware and Architectures for Parallelism
   * Multicore Processors
   * Graphics Processing Units (GPUs)
       CUDA
       OpenCL
   * Clusters and Supercomputers

### Performance Analysis and Optimization
   * Performance Metrics
   * Amdahl's Law and Gustafson's Law
   * Profiling and Benchmarking
   * Parallel Performance Tuning

## File I/O
### I. Introduction to File I/O
   * What is File I/O?
   * Importance of File I/O in programming
   * Types of files: text and binary
   * File encoding and character sets

### Reading and Writing Files
   * Opening and closing files
       File modes (read, write, append)
       Error handling and exceptions
   * Reading from files
       Reading the entire file
       Reading a specific number of bytes or characters
       Reading line by line
       File iterators
   * Writing to files
       Writing data to a file
       Writing line by line
       Truncating and overwriting files

### File Manipulation
   * File metadata
       File size
       File permissions
       File timestamps
   * File and directory operations
       Renaming and moving files
       Deleting files
       Creating directories
       Listing directory contents
       Removing directories

### Working with Text Files
   * String manipulation and formatting
   * Regular expressions
   * Parsing structured text formats
       CSV
       JSON
       XML

### Working with Binary Files
   * Binary file formats
   * Reading and writing binary data
   * Endianness
   * Binary file manipulation

### Serialization and Deserialization
   * What is serialization and deserialization?
   * Serialization formats
       Binary serialization
       JSON serialization
       XML serialization
   * Custom serialization and deserialization methods

### File I/O Performance
   * Buffering and caching
   * Asynchronous File I/O
   * File I/O performance tuning and best practices
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

## Introduction to Reactive Programming
- What is reactive programming?
- Benefits of reactive programming
- Comparison to imperative and functional programming

## Core Concepts of Reactive Programming
- Data streams
- Observables and observers
- Subscriptions
- Subjects

## Functional Programming Basics
- Pure functions
- Higher-order functions
- Immutability
- Functional composition

## Reactive Programming Operators
- Creating observables
- Transforming observables
- Filtering observables
- Combining observables
- Error handling and recovery

## Reactive Programming in Practice
- Handling user input
- Reactive data fetching and state management
- Real-time updates and live data
- Backpressure and buffering strategies

## Reactive Programming Libraries and Frameworks
- Overview of popular libraries and frameworks
- Reactive Extensions (Rx)
- Reactive Streams implementations (e.g., Reactor, Akka Streams)
- Language-specific reactive libraries (e.g., RxJava, RxJS, RxDart)

## Reactive Architectures and Patterns
- Event-driven architecture
- Microservices and reactive systems
- Command Query Responsibility Segregation (CQRS) and Event Sourcing
- Reactive design patterns

## Testing Reactive Applications
- Unit testing observables and operators
- Integration testing reactive components
- End-to-end testing reactive applications
- Debugging and troubleshooting

## Performance and Optimization
- Measuring performance in reactive applications
- Optimizing data streams and operators
- Concurrency and parallelism in reactive systems
- Resource management and best practices

