
// Define a const
const val USER_TYPE = 1
const val STRING1 = "This is a string 1"

fun main(args: Array<String>){
    // Print one by line
    println("1. println ")
    println("2. println ")

    // Print oll in one line
    print("1. print ")
    print("2. print")

    // Define a variable
    val score = 12.3

    println("score")
    println("$score")
    println("score = $score")
    println("${score + score}")


    println("value of USER_TYPE: ${USER_TYPE}")
    // Formating string
    println(String.format("value of USER_TYPE: %s ", STRING1))

    val highestScore: Long = 9999
    println("$highestScore")

    var highestScore2 = 9999
    println("$highestScore2")

    val distance = 10000000000  // distance variable of type Long
    val distance2 = 100L    // distance value of type Long

    println("$distance")
    println("$distance2")

    val distance3 = 19.5F
    println("$distance3")

}