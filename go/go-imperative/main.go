package main

import "fmt"

func main() {
	// Define an integer constant
	const LENGTH int = 10

	// Define an string constant

	const MESSAGE = "HI CONST"

	// Task Print string
	fmt.Print(" Simple string")

	// Task Print string with new lines
	fmt.Print("\n Simple \n string \n")

	// Task Print with multiple variables

	fmt.Print("\n", "string 1", " - string 2", " - string 3 \n")

	fmt.Print(MESSAGE)
	fmt.Print(LENGTH, "\n")

	// Println with new line
	fmt.Println(MESSAGE)
	fmt.Println(LENGTH)

	fmt.Println("**************")
	fmt.Printf("%v\n", MESSAGE)
	fmt.Printf("%#v\n", MESSAGE)
	fmt.Printf("%T\n", MESSAGE)

	fmt.Println("**************")
	fmt.Printf("%v\n", LENGTH)
	fmt.Printf("%#v\n", LENGTH)
	fmt.Printf("%T\n", LENGTH)
	fmt.Printf("%v%%\n", LENGTH)

	// Define integer explicit way
	var i int = 10
	// Define integer implicit way
	i2 := 11

	fmt.Println("*** i")
	fmt.Printf("%v\n", i)
	fmt.Printf("%T\n", i)

	fmt.Println("*** i2")
	fmt.Printf("%v\n", i2)
	fmt.Printf("%T\n", i2)

	// Define floar explicit way
	var f32 float32 = 10.0
	// Define float implicit way
	var f64 float64 = 11.0

	fmt.Println("*** float 32")
	fmt.Printf("%v\n", f32)
	fmt.Printf("%T\n", f32)

	fmt.Println("*** float 64")
	fmt.Printf("%v\n", f64)
	fmt.Printf("%T\n", f64)

	// Define boolean explicit way
	var b1 bool = true
	// Define float implicit way
	var b2 bool = false

	fmt.Println("*** boolean")
	fmt.Printf("b1 value: %v\n", b1)
	fmt.Printf("b1 type: %T\n", b1)

	fmt.Printf("b2 value: %v\n", b2)
	fmt.Printf("b2 type: %T\n", b2)

	// Define String explicit way
	var s1 string = "string 1"
	// Define Sgtring implicit way
	var s2 string = "string 2"

	fmt.Println("*** String")
	fmt.Printf("b1 value: %v\n", s1)
	fmt.Printf("b1 type: %T\n", s1)

	fmt.Printf("b2 value: %v\n", s2)
	fmt.Printf("b2 type: %T\n", s2)
}
