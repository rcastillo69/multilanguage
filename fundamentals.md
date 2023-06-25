
## Basic Features
- Program outputs and Comments
    - Main
    - Comments
      - Single Line
      - Multiple Lines
    - Console Output
    - Compile / Debug
    - Output Console
        - Format output   

## Variables & System Types

### System data types

#### Primitive types & Variables, values
- Constant
- Numbers
    - Integer 32/64 bits
        - Signed
        - Unsigned
- Floating Point 32/64
- Boolean
- Date, Time & Datetime
- String
  - multiline
  - Concatenation
- Char

- Declaring Variables
    - Explicit
    - Implicit
- Group of declarations
- Multiple declarations inline
- Check Type
- Casting Data Types
- Mutability / Immutability

#### Special types
- Null value
- Pointers & Address

#### Operators

- Arithmetic operators: used to perform basic mathematical operations, such as addition (+), subtraction (-), multiplication (-), division (/), modulus or remainder (%), increment (++) and decrement (--).

- Assignment operators: used to assign values to variables, such as the assignment operator (=) and other compound assignment operators such as +=, -=, -=, /=, %=.

- Comparison operators: used to compare values, such as equality (==), inequality (!=), greater than (>), less than (<), greater than or equal to (>=) and less than or equal to (<=).

- Logical operators: used to perform Boolean operations, such as the logical operator and (&&), the logical operator or (||), and the logical negation operator (!).
Bitwise operators: used to perform bitwise operations, such as the left shift operator (<<), the right shift operator (>>), the bitwise and operator (&), the bitwise or operator (|), and the bitwise negation operator (~).

- Concatenation operators: used to concatenate character strings or values, such as the concatenation operator (+).

- Conditional operators: used to assign values to a variable based on a condition, such as the ternary conditional operator (?).

## Flow
### Decision
    - Simple
    - Nested
    - Multiple
### Loop
    - Simple
        - While
        - Loop
        - For
    - Continue & Escaping

#### Composite types
- Enum
  - Operations
- Structure or Record
  - Operations
- Slice
  - Operations
- Array
  - Operations
  - Vector
    - Operations
  -  Multi-dimensional arrays
     -  Operations
- Tuples
  - Operations
- Dictionaries or Maps
  - Operations
- Lists
- Sets


## Functions
    - Declaration
    - Function parameters and arguments
    - Function return values
    - Recursion

## Error Handling
### Introduction to Error Handling
   - What is Error Handling?
   - Importance of Error Handling in programming
   - Types of errors: compile-time, runtime, and logical errors

### Basic Error Handling Techniques
   - Return values and error codes
   - Error handling functions and methods
   - Assertions

### Exceptions
   - What are exceptions?
   - Exception hierarchy and built-in exceptions
   - Creating custom exceptions

### Try-Catch-Finally Blocks
   - The try block: capturing exceptions
   - The catch block: handling exceptions
       Catching specific exceptions
       Catching multiple exceptions
   - The finally block: executing code regardless of exception occurrence
   - Nested try-catch-finally blocks

### Raising and Throwing Exceptions
   - Raising exceptions
   - Throwing exceptions

### Resource Management and Cleanup
   - Proper resource allocation and deallocation
   - Using with statements (context managers) for resource management

## Best Practices for Error Handling
   - Defensive programming
   - Handling exceptions at the appropriate level
   - Providing meaningful error messages and logging
   - Failing fast and early
   - Testing and debugging strategies



## Concurrency, Multithreading, and Parallelism

### Introduction to Concurrency and Parallelism
   - What is Concurrency?
   - What is Parallelism?
   - Importance and benefits of Concurrency and Parallelism
   - Concurrency vs. Parallelism

### Multithreading
   - Introduction to Threads
       What is a Thread?
       Threads vs. Processes
   - Creating Threads
       Thread creation in different programming languages
       Thread lifecycle
   - Thread Synchronization
       Race conditions
       Critical sections
       Mutexes and Locks
       Semaphores
       Monitors and Condition Variables
   - Deadlocks
       Deadlock causes and detection
       Deadlock prevention
       Deadlock avoidance

### Parallel Programming
   - Parallel Programming Models
       Data parallelism
       Task parallelism
       Pipeline parallelism
   - Parallel Programming Constructs
       Fork-join
       MapReduce
       Parallel loops
       Parallel aggregations
   - Load Balancing
       Static vs. dynamic load balancing
       Work stealing

### Concurrent Data Structures
   - Introduction to Concurrent Data Structures
   - Lock-based Data Structures
   - Lock-free Data Structures
   - Wait-free Data Structures

### Asynchronous Programming
   - Asynchronous vs. Synchronous Programming
   - Callbacks
   - Promises and Futures
   - Async/Await
   - Event-driven Programming

### Message Passing and Distributed Systems
   - Message Passing Interface (MPI)
   - Actor Model
   - Remote Procedure Calls (RPC)
   - Publish-Subscribe Pattern

### Hardware and Architectures for Parallelism
   - Multicore Processors
   - Graphics Processing Units (GPUs)
       CUDA
       OpenCL
   - Clusters and Supercomputers

### Performance Analysis and Optimization
   - Performance Metrics
   - Amdahl's Law and Gustafson's Law
   - Profiling and Benchmarking
   - Parallel Performance Tuning

## File I/O
### I. Introduction to File I/O
   - What is File I/O?
   - Importance of File I/O in programming
   - Types of files: text and binary
   - File encoding and character sets

### Reading and Writing Files
   - Opening and closing files
       File modes (read, write, append)
       Error handling and exceptions
   - Reading from files
       Reading the entire file
       Reading a specific number of bytes or characters
       Reading line by line
       File iterators
   - Writing to files
       Writing data to a file
       Writing line by line
       Truncating and overwriting files

### File Manipulation
   - File metadata
       File size
       File permissions
       File timestamps
   - File and directory operations
       Renaming and moving files
       Deleting files
       Creating directories
       Listing directory contents
       Removing directories

### Working with Text Files
   - String manipulation and formatting
   - Regular expressions
   - Parsing structured text formats
       CSV
       JSON
       XML

### Working with Binary Files
   - Binary file formats
   - Reading and writing binary data
   - Endianness
   - Binary file manipulation

### Serialization and Deserialization
   - What is serialization and deserialization?
   - Serialization formats
       Binary serialization
       JSON serialization
       XML serialization
   - Custom serialization and deserialization methods

### File I/O Performance
   - Buffering and caching
   - Asynchronous File I/O
   - File I/O performance tuning and best practices

