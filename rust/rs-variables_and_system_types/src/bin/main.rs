mod main_input;

use std::any::type_name;
use chrono::prelude::*;

// function to determine Var type
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
    println!("Var x {}", x);

    // Task define integer 64
    let x64:i64 = 64;
    println!("type of x64 {}", type_of(&x64));
    println!("Var x64 {}", x);

    // Task define a unsigned integer
    let xu8:u8 = 8;
    let xu16:u16 = 16;
    let xu32:u32 = 32;
    let xu64:u64 = 64;
    let xu128:u128 = 132;

    println!("Var xu8 {}", xu8);
    println!("Var xu16 {}", xu16);
    println!("Var xu32 {}", xu32);
    println!("Var xu64 {}", xu64);
    println!("Var xu128 {}", xu128);

    // Task define a floating point number
    let xf32:f32 = 32.0;
    let xf64:f64 = 64.0;
    println!("type of xf32 {}", type_of(&xf32));
    println!("Var xf32 {}", xf32);
    println!("type of xf64 {}", type_of(&xf64));
    println!("Var xf64 {}", xf64);

    // Task boolean
    let is_valid:bool = true;
    println!("type of isValid {}", type_of(&is_valid));
    println!("Var isValid {}", is_valid);

    // Task: Date, Time & DateTime
    let date =  NaiveDate::from_ymd_opt(2014, 7, 8).unwrap();
    let time = NaiveTime::from_hms_opt(12,30,00);
    let datetime = NaiveDateTime::new(date,time.unwrap());
    print!("date:{}",date ); 
    print!("time:{}",time.unwrap() );
    print!("datetime:{}",datetime );
    

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
    let content_string = String::from("Rust is beautiful");
    println!("empty_string the length is {}",empty_string.len());
    println!("content_string the length is {}",content_string.len());

    // Task Concatenation
    let mut greeting = "Hi ".to_string();
    greeting.push_str("Rust");
    println!("greeting = {}",greeting);

    // Task Char
    let letter:char = 'a';
    println!("type of letter {}", type_of(&letter));
    println!("Var letter {}", letter);

    // Type of declaration
    
    // Explicit type declaration
    let explicit_var: i32 = 42;
    println!("explicit var: {}", explicit_var);

    // Implicit type declaration
    let implicit_var = "Hello, world!";
    println!("implicit var: {}",implicit_var);

    // Implicit grouped declaration
    let (x, y, z) = (1, 2, 3);
    println!("x = {}, y = {}, z = {}", x, y, z);

    // No exist declarations on group
    let a = 4;
    let b = 5;
    let c = 6;
    println!("a = {}, b = {}, c = {}", a, b, c);

   // Conversion int a float
   let my_int: i32 = 42;
   let my_float: f32 = my_int as f32;
   println!("The var float is : {}", my_float);

   // Conversion int a string
   let my_int_string: String = my_int.to_string();
   println!("The var string is : {}", my_int_string);

   // Conversion float a string
   let my_float: f32 = 3.14159;
   let my_float_string: String = my_float.to_string();
   println!("The var string is : {}", my_float_string);

   // Conversion string to int
   let my_string: &str = "42";
   let my_int: i32 = my_string.parse().unwrap();
   println!("The var int is : {}", my_int);

   // Conversion string a float
   let my_string: &str = "3.14159";
   let my_float: f32 = my_string.parse().unwrap();
   println!("The var float is : {}", my_float);

   // Conversion Date to string
   let my_date: Option<NaiveDate> = NaiveDate::from_ymd_opt(2023, 5, 3);
   let my_date_string: String = my_date.unwrap().format("%Y-%m-%d").to_string();
   println!("The var string is : {}", my_date_string);

   // Conversion string to date
   let my_string: &str = "2023-05-03";
   let my_date: NaiveDate = NaiveDate::parse_from_str(my_string, "%Y-%m-%d").unwrap();
   println!("The var date is : {}", my_date);

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

    // Var immutable
    let my_immutable_variable: i32 = 42;
    println!("The value of immutable var is: {}", my_immutable_variable);

    // Error when trying to modify a variable
    // my_immutable_variable = 43;

    // Var mutable
    let mut my_mutable_variable: i32 = 42;
    println!("The value of mutable var is: {}", my_mutable_variable);

    // Modify mutable variable
    my_mutable_variable = 43;
    println!("The value of mutable var updated is: {}", my_mutable_variable);


  // define a variable & a pointer to it

  let mut my_variable: i32 = 42;
  let my_pointer: &mut i32 = &mut my_variable;

  // Modify the variable through the pointer
  *my_pointer = 43;

  // Print the variable
  println!("The value of pointer is : {}", &my_variable);

  // Define a null variable
  let my_null_variable: Option<i32> = None;

  // Print the variable
  match my_null_variable {
      Some(value) => println!("The value of the variable is: {}", value),
      None => println!("The variable is null"),
  }

}