
fn main(){
    // loop statement
    let mut count = 0;
    loop{
        count +=1;
        if count == 5 {
            println!("Loop stops at count {}", count);
            break;
        }
    }

    // While loop
    let mut n = 6;
    while  n != 0 {
        println!("{}!", n);
        n -=1;
    }
    println!("End while");

    // For loop
    let a = [10, 20, 30, 40, 50];
    for element in a.iter() {
        println!("the value is: {}", element);
    }
    println!("Loop 2!!!");
    // For loop
    let a = [10, 20, 30, 40, 50];
    for element in a {
        println!("the value is: {}", element);
    }
    println!("Loop 3!!!");
    // For loop with range
    for number in (1..4).rev() {
        println!("{}!", number);
    }
    println!("GO!!!");

    // Mutable looping
    println!("Vector");
    let mut vec1 = vec![1,2,3,4,5];
    for num in &mut vec1{
        *num +=1;
    }
    println!("Vector modified");
    for n in vec1{
        println!("n= {}",n);
    }

    // Returning value using loop
    let mut count  = 0;
    let final_value = loop{
        count += 1;
        if count > 10 {
            break count +1;
        }
    };
    println!("final value {}",final_value);

    // Match statement
    let state = "happy";
    match state {
        "happy" => println!("State is happy"),
        "sad" => println!("State is sad"),
        _ => println!("State is unknown"),
    }

    // Match using enum
    enum MessageState {
        Pernding,
        Sending,
        Received
    }

    let status = MessageState::Pernding;
    
    match status {
        MessageState::Pernding => println!("Message pending!"),
        MessageState::Sending => println!("Message sending!"),
        MessageState::Received => println!("Message received!")
    }

}