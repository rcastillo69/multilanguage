#include <iostream>

int main(){
    double f,c;
    std::cout << "Enter a Fahrenheit value: ";
    std::cin >> f;

    // Convert
    c = (f - 32) * 5.0 / 9.0;

    std::cout << f << " degrees Fahrenheit is " << c << " degrees Celsius\n";

    return 0;

}