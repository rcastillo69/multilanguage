use std::any::type_name;

// function to determine variable type
fn type_of<T>(_: T) -> &'static str {
    type_name::<T>()
}

fn main(){

    // Task define a constant
    const USER_LIMIT:i32 = 100;
    const USER_MIN:i32 = 10;
    println!("User limit: {}", USER_LIMIT );
    println!("User min: {}", USER_MIN );

    // Task define integer 32
    let x:i32 = 21;
    println!("type of x {}", type_of(&x));
    println!("variable x {}", x);

    // Task define integer 64
    let x64:i64 = 64;
    println!("type of x64 {}", type_of(&x64));
    println!("variable x64 {}", x);

    // Task define a unsigned integer
    let xu8:u8 = 8;
    let xu16:u16 = 16;
    let xu32:u32 = 32;
    let xu64:u64 = 64;
    let xu128:u128 = 132;

    println!("variable xf32 {}", xu8);
    println!("variable xf32 {}", xu16);
    println!("variable xf32 {}", xu32);
    println!("variable xf32 {}", xu64);
    println!("variable xf32 {}", xu128);

    // Task define a unsigned integer
    let xf32:f32 = 32.0;
    let xf64:f64 = 64.0;
    println!("type of xf32 {}", type_of(&xf32));
    println!("variable xf32 {}", xf32);
    println!("type of xf64 {}", type_of(&xf64));
    println!("variable xf64 {}", xf64);

    // Task define a string
    // String literal
    let company:&str="My company";
    let location:&str = "Australia";
    println!("Company is : {} Location :{}",company,location);

    let company2:&'static str = "Company";
    let location2:&'static str = "Argentina";
    println!("Company2 is : {} Location2 :{}",company2,location2);

    // String object
    let empty_string = String::new();
    let content_string = String::from("Rust is beatiful");
    println!("empty_string the length is {}",empty_string.len());
    println!("content_string the length is {}",content_string.len());

    // Task Char
    let letter:char = 'a';
    println!("type of letter {}", type_of(&letter));
    println!("variable letter {}", letter);

    // Task Concatenation
    let mut greeting = "Hi ".to_string();
    greeting.push_str("Rust");
    println!("greeting = {}",greeting);

    // Task boolean
    let is_valid:bool = true;
    println!("type of isValid {}", type_of(&is_valid));
    println!("variable isValid {}", is_valid);

    // Task Enum
    // The `derive` attribute automatically creates the implementation
    // required to make this `enum` printable with `fmt::Debug`.
    #[derive(Debug)]
    enum GenderCategory {
        Male,Female
    }

    let male = GenderCategory::Male;
    let female = GenderCategory::Female;
    println!("{:?}",male);
    println!("{:?}",female);

    let x = 5;
    let raw = &x as *const i32;
    let points_at = unsafe { *raw };
    println!("raw points at {}", points_at);




/*
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





    let y = 2.5;
    let s ="string1";
    let b = true;
    println!("type of x {}", type_of(&y));
    println!("variable y {}", x);
    println!("variable s {}", s);
    println!("variable b {}", b);


*/
}