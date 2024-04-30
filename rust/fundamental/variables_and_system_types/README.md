# Rust imperative


## Rust Output Functions

Rust has two functions to output text:

- print!: same as format! but the text is printed to the console (io::stdout).
- println!: same as print! but a newline is appended.


Prints to the standard output, with a newline.

	pprintln!("{} days", 31);
	println!("{0}, this is {1}. {1}, this is {0}", "Alice", "Bob");
	println!("{subject} {verb} {object}",
             object="the lazy dog",
             subject="the quick brown fox",
             verb="jumps over");


## Declaring constant
Constants refer to fixed values that the program may not alter during its execution

	Syntax:
		const VARIABLE_NAME:dataType = value;

## Declaring Var

- Use the var keyword, followed by Var name and type:

	Syntax:

		let variable_name:dataType = value; //type specified

- With the := sign

	Syntax:
		
		let variable_name = value; // no type specified
