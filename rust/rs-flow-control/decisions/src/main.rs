fn main() {
    // while loop example
    let mut i = 0;
    println!("while loop:");
    while i < 5 {
        println!("{}", i);
        i += 1;
    }

    // for loop example
    println!("\nfor loop:");
    for j in 0..5 {
        println!("{}", j);
    }

    // Simulating do-while loop using loop
    println!("\nSimulated do-while loop:");
    let mut k = 0;
    loop {
        println!("{}", k);
        k += 1;
        if k >= 5 {
            break;
        }
    }

    // continue in loop
    println!("\ncontinue in loop:");
    for l in 0..5 {
        if l == 2 { continue; }
        println!("{}", l);
    }

    // break in loop
    println!("\nbreak in loop:");
    for m in 0..5 {
        if m == 3 { break; }
        println!("{}", m);
    }

    // nested loops with break
    println!("\nnested loops with break:");
    for n in 0..3 {
        for o in 0..3 {
            if o == 1 { break; }
            println!("n={}, o={}", n, o);
        }
    }

    // breaking out of all nested loops
    println!("\nbreaking out of all nested loops:");
    'outer: for p in 0..3 {
        for q in 0..3 {
            if q == 1 {
                break 'outer;
            }
            println!("p={}, q={}", p, q);
        }
    }
}
