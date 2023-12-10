#include <iostream>
#include <string>
#include <chrono>
#include <iomanip>


int main() {
    // Integer type
    int myInt = 10;
    std::cout << "Integer: " << myInt << std::endl;

    // Floating point type
    float myFloat = 3.14f;
    std::cout << "Float: " << myFloat << std::endl;

    // Double type
    double myDouble = 9.82;
    std::cout << "Double: " << myDouble << std::endl;

    // Character type
    char myChar = 'A';
    std::cout << "Character: " << myChar << std::endl;

    // Boolean type
    bool myBool = true;
    std::cout << "Boolean: " << (myBool ? "true" : "false") << std::endl;

    // String type (using the string class from the standard library)
    std::string myString = "Hello, World!";
    std::cout << "String: " << myString << std::endl;

    // Unsigned int
    unsigned int myUnsignedInt = 3000000000U;
    std::cout << "Unsigned Integer: " << myUnsignedInt << std::endl;

    // Long type
    long myLong = 123456789L;
    std::cout << "Long: " << myLong << std::endl;

    // Long long type
    long long myLongLong = 123456789012345LL;
    std::cout << "Long long: " << myLongLong << std::endl;

    // Short type
    short myShort = 32767;
    std::cout << "Short: " << myShort << std::endl;

     // Constant type
    const int myConstInt = 42;
    std::cout << "Constant Integer: " << myConstInt << std::endl;

    // Printing current date using <chrono> and <iomanip>
    auto now = std::chrono::system_clock::now();
    auto in_time_t = std::chrono::system_clock::to_time_t(now);

    std::cout << "Current Date: ";
    std::cout << std::put_time(std::localtime(&in_time_t), "%Y-%m-%d") << std::endl;


    return 0;
}
