# Go imperative


## Go Output Functions

Go has three functions to output text:

* Print()
* Println()
* Printf()

### The Print() Function
The Print() function prints its arguments with their default format.

### The Println() Function
The Println() function is similar to Print() with the difference that a whitespace is added between the arguments, and a newline is added at the end

### The Printf() Function
The Printf() function first formats its argument based on the given formatting verb and then prints them

#### General Formatting Verbs
The following verbs can be used with all data types:

| Verb |	Description|
| ----------- | ----------- |
|%v	|Prints the value in the default format|
|%#v	|Prints the value in Go-syntax format|
|%T	|Prints the type of the value|
|%%	|Prints the % sign|


## Declaring constant
Constants refer to fixed values that the program may not alter during its execution

	Syntax:
		const variable type = value

## Declaring variable

- Use the var keyword, followed by variable name and type:

	Syntax:

		var variablename type = value

- With the := sign

	Syntax:
		
		variablename := value
