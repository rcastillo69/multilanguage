use std::io::stdin;

fn main(){
    let mut message: String = String::new();
    println!("Enter your message");

    stdin().read_line(&mut message).unwrap();

    println!("Message received :{}",message);

}