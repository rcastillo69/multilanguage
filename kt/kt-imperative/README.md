# Kotlin imperative


## Kotlin Output Functions

Kotlin has two functions to output text:

* Print()
* Println()


### The Print() Function
The Print() function prints its arguments with their default format.

### The Println() Function
The Println() function is similar to Print() with the difference that a whitespace is added between the arguments, and a newline is added at the end


#### General Formatting Verbs
Kotlin borrows the String.format() method from the Java language, so you can format your string values with it.

| Verb |	Description|
| ----------- | ----------- |
| %b | Boolean |
| %c | Character |
| %d | Signed Integer |
| %e | Float in Scientific Notation |
| %f | Float in Decimal Format|
| %g | Float in Decimal or Scientific Notation, depending on the value|
| %h | Hashcode of the supplied argument|
| %n | Newline separator|
| %o | Octal Integer (base 8)|
| %s | String|
| %t | Date or Time|
| %x | Hexadecimal Integer (base 16)|


## Declaring constant
Constants refer to fixed values that the program may not alter during its execution

	Syntax:
		const val name = value

## Declaring variable

Kotlin variables are created using either var or val keywords and then an equal sign = is used to assign a value to those created variables.

- Syntax Explicit

      var variablename : type = value

- Syntax Implicit

      var variablename = value

### Kotlin Mutable Variables
Mutable means that the variable can be reassigned to a different value after initial assignment.

    var name = "Zara Ali"

    var age = 19 
   
### Kotlin Read-only Variables
A read-only variable can be declared using val (instead of var) and once a value is assigned, it can not be re-assigned.

    val name = "Zara Ali"
    val age = 19


### Difference Between var and val
val (Immutable reference) - The variable declared using val keyword cannot be changed once the value is assigned. It is similar to final variable in Java.
var (Mutable reference) - The variable declared using var keyword can be changed later in the program. It corresponds to regular Java variable.