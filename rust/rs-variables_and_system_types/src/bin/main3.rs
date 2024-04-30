
fn main (){
    // Conditionals
    let number = 18;

    // Basid if statement
    if number % 2 == 0{
        println!("{} is even", number)
    } else {
        println!("{} is odd", number)
    }

    // Using if in a let statement
    let description = if number % 2 == 0 { "even"} else {"odd"};
    println!("{} is {}", number, description);

    // Multiple conditions with else if
    if number % 5 == 0{
        println!("{} is divisible by 5", number)
    } else if number % 3 == 0{
        println!("{} is divisible by 3", number)
    } else {
        println!("{} is not divisible by 5 and 3", number)
    }
}