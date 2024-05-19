package main

import (
	"fmt"
)

func is_divisibility_by(number int, div_by int) bool {
	return number%div_by == 0
}

func is_leap(year_input int) bool {
	return is_divisibility_by(year_input, 4) &&
		(!is_divisibility_by(year_input, 100) || is_divisibility_by(year_input, 400))

}

func main() {
	var input int
	fmt.Scanf("%v\n", &input)

	fmt.Println(is_leap(input))
}
