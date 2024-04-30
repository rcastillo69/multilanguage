//
// Created by rcastillo on 24/02/24.
//

#include <string>
#include <iostream>

int main() {
    // Task define a constant
    const int MAX_USER = 32;
    std::cout << "Value of: " << MAX_USER << std::endl;
    std::cout << "Type of MAX_USER: " << typeid(MAX_USER).name() << std::endl;

    const char char1 = 'A';
    std::cout << "Value of: " << char1 << std::endl;
    std::cout << "Type of char1: " << typeid(char1).name() << std::endl;


    const float float1 = 3.14L;
    const double double1 = 3.14159;
    const bool bool1 = true;
    const char* char2 = "Hello World";
    const std::string string1 = "Hello world 2";

    // Mutable & inmutables
    const int MAX = 32;
    int MAX2 = 33;

    // Chars
    char myChar = 'a';
    wchar_t myWchar = L'a';
    char16_t myChar16 = u'a';
    char32_t myChar32 = U'a';

    //Floating-point
    float myFloat = 1.0f;
    double myDouble = 2.0;
    long double myLongDouble = 3.0;

    // Boolean
    bool myBool = true;

    // Compound Types
    // Pointers
    int* myPointer = nullptr;
    // References
    int myVariable = 10;
    int& myReference = myVariable;









    return 0;


}