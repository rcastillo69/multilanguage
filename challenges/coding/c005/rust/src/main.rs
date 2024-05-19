use std::io;

fn is_divisibility_by(number:i32, div_by:i32) -> bool{
    number & div_by == 0
}

fn is_leap(year_input:i32)-> bool{
    is_divisibility_by(year_input, 4) &&
    (!is_divisibility_by(year_input, 100) || is_divisibility_by(year_input, 400))
}

fn main() {
    let mut year_input = String::new();

    io::stdin().read_line(&mut year_input).expect("Failed to read line");

    // Parse input to integer
    let year:i32 = year_input.trim().parse().expect("Invalid integer 32");

    println!("{}", is_leap(year));
}
