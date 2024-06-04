
fun solveMeFirst(a: Int, b: Int): Int {
    return a + b
}

fun main() {
    println("Please enter the first integer:")
    val firstInput = readlnOrNull()
    val firstNumber = firstInput?.toIntOrNull()

    println("Please enter the second integer:")
    val secondInput = readlnOrNull()
    val secondNumber = secondInput?.toIntOrNull()

    if (firstNumber != null && secondNumber != null) {
        val result = solveMeFirst(firstNumber, secondNumber)
        println("Result is: $result")
    } else {
        println("Invalid input. Please enter valid integers.")
    }
}
