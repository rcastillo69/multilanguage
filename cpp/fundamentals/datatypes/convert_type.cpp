#include <iostream>
#include <string>
#include <chrono>
#include <iomanip>
#include <sstream>

int main() {
    // char to int and float
    char ch = '5';
    int charToInt = ch - '0'; // Convert char to int
    float charToFloat = static_cast<float>(charToInt); // Convert int to float

    std::cout << "char to int: " << charToInt << std::endl;
    std::cout << "char to float: " << charToFloat << std::endl;

    // string to int, float, and double
    std::string str = "123.45";
    int stringToInt = std::stoi(str); // Convert string to int
    float stringToFloat = std::stof(str); // Convert string to float
    double stringToDouble = std::stod(str); // Convert string to double

    std::cout << "string to int: " << stringToInt << std::endl;
    std::cout << "string to float: " << stringToFloat << std::endl;
    std::cout << "string to double: " << stringToDouble << std::endl;

    // int to float and double
    int num = 42;
    float intToFloat = static_cast<float>(num); // Convert int to float
    double intToDouble = static_cast<double>(num); // Convert int to double

    std::cout << "int to float: " << intToFloat << std::endl;
    std::cout << "int to double: " << intToDouble << std::endl;

    // Current DateTime as string
    auto now = std::chrono::system_clock::now();
    auto in_time_t = std::chrono::system_clock::to_time_t(now);

    std::stringstream ss;
    ss << std::put_time(std::localtime(&in_time_t), "%Y-%m-%d %H:%M:%S");
    std::string dateTimeStr = ss.str();

    std::cout << "Current DateTime: " << dateTimeStr << std::endl;

    return 0;
}
