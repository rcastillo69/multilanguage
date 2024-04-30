#include <iostream>

int main() {
    // Arithmetic Operators
    int a = 10, b = 3;
    std::cout << "Arithmetic Operators:" << std::endl;
    std::cout << "a + b = " << (a + b) << std::endl;
    std::cout << "a - b = " << (a - b) << std::endl;
    std::cout << "a * b = " << (a * b) << std::endl;
    std::cout << "a / b = " << (a / b) << std::endl; // Integer division
    std::cout << "a % b = " << (a % b) << std::endl;
    std::cout << std::endl;

    // Comparison Operators
    std::cout << "Comparison Operators:" << std::endl;
    std::cout << "a == b: " << (a == b) << std::endl;
    std::cout << "a != b: " << (a != b) << std::endl;
    std::cout << "a > b: " << (a > b) << std::endl;
    std::cout << "a < b: " << (a < b) << std::endl;
    std::cout << "a >= b: " << (a >= b) << std::endl;
    std::cout << "a <= b: " << (a <= b) << std::endl;
    std::cout << std::endl;

    // Assignment Operators
    std::cout << "Assignment Operators:" << std::endl;
    a += b; // a = a + b;
    std::cout << "a += b: " << a << std::endl;
    a -= b; // a = a - b;
    std::cout << "a -= b: " << a << std::endl;
    // Other assignment operators include *=, /=, %=, <<=, >>=, &=, ^=, |=
    std::cout << std::endl;

    // Logical Operators
    bool x = true, y = false;
    std::cout << "Logical Operators:" << std::endl;
    std::cout << "x && y: " << (x && y) << std::endl;
    std::cout << "x || y: " << (x || y) << std::endl;
    std::cout << "!x: " << (!x) << std::endl;
    std::cout << std::endl;

    // Bitwise Operators
    int m = 5, n = 2; // 5 = 0101, 2 = 0010 in binary
    std::cout << "Bitwise Operators:" << std::endl;
    std::cout << "m & n: " << (m & n) << std::endl;
    std::cout << "m | n: " << (m | n) << std::endl;
    std::cout << "m ^ n: " << (m ^ n) << std::endl;
    std::cout << "~m: " << (~m) << std::endl;
    std::cout << "m << 1: " << (m << 1) << std::endl;
    std::cout << "m >> 1: " << (m >> 1) << std::endl;
    std::cout << std::endl;

    // Increment/Decrement Operators
    int z = 0;
    std::cout << "Increment/Decrement Operators:" << std::endl;
    std::cout << "z++: " << z++ << std::endl; // Post-increment
    std::cout << "++z: " << ++z << std::endl; // Pre-increment
    std::cout << "z--: " << z-- << std::endl; // Post-decrement
    std::cout << "--z: " << --z << std::endl; // Pre-decrement

    return 0;
}
