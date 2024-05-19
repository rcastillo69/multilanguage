package main

import (
	"fmt"
	"strconv"
	"strings"
)

func getHours(hh string) int {
	value, _ := strconv.Atoi(hh)
	return value
}

func getTime(input string) string {
	return input[:len(input)-2]
}

func getPartsTime(input string) []string {
	return strings.Split(getTime(input), ":")
}

func getMeridian(input string) string {
	return input[len(input)-2:]
}

func getMilitarTime(partstime []string) string {
	return partstime[0] + ":" + partstime[1] + ":" + partstime[2]
}

func timeConversion(input string) string {
	meridian := strings.ToUpper(getMeridian(input))
	partstime := getPartsTime(input)

	if meridian == "PM" && getHours(partstime[0]) < 12 {
		partstime[0] = strconv.Itoa(getHours(partstime[0]) + 12)
	}

	if meridian == "AM" && getHours(partstime[0]) == 12 {
		partstime[0] = "00"
	}

	return getMilitarTime(partstime)

}

func main() {
	var input string
	fmt.Scanf("%v\n", &input)

	fmt.Println(timeConversion(input))
}
