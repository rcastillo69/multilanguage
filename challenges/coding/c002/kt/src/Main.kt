fun getMilitaryTime(parts: List<String>): String{
      return parts[0]+ ":" +parts[1]+ ":" +parts[2]
}

fun getMeridian(text: String?): String {
    val value = text ?: ""
    return value.takeLast(2).uppercase()
}

fun getParts(input: String?): List<String> {
    val value = input ?: ""
    return value.split(":")
}

fun main() {
    println("Enter the date:")
    val dateInput = readlnOrNull()
    val parts = getParts(dateInput).toMutableList()
    if (getMeridian(dateInput)== "PM" && parts[0].toInt() <12){
        parts[0] = (parts[0].toInt() + 12).toString()
    }
    if (getMeridian(dateInput)== "AM" && parts[0].toInt() ==12){
        parts[0] = "00"
    }

    print(getMilitaryTime(parts))





}