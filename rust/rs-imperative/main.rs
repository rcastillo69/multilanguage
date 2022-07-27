use std::any::type_name;

// function to determine variable type
fn type_of<T>(_: T) -> &'static str {
    type_name::<T>()
}

fn main(){

    print!("Print {}", "Hi\n");

    // Print with parameters
    println!("{0}, this is {1}. {1}, this is {0} \n", "Alice", "Bob");

    // As can named arguments.
    println!("{subject} {verb} {object}",
             object="the lazy dog",
             subject="the quick brown fox",
             verb="jumps over");

    // Different formatting can invoked by specified format character after a
    // `:`.
    println!("Base 10 repr:               {}",   69420);
    println!("Base 2 (binary) repr:       {:b}", 69420);
    println!("Base 8 (octal) repr:        {:o}", 69420);
    println!("Base 16 (hexadecimal) repr: {:x}", 69420);
    println!("Base 16 (hexadecimal) repr: {:X}", 69420);

     
    const USER_LIMIT:i32 = 100;
    const USER_MIN:i32 = 10;
    
    println!("User limit: {}", USER_LIMIT );
    println!("User min: {}", USER_MIN );

    let x = 21;
    let y = 2.5;
    let s ="string1";
    let b = true;
    println!("type of x {}", type_of(&y));
    println!("variable y {}", x);
    println!("variable s {}", s);
    println!("variable b {}", b);



}