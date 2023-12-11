#include <iostream>

int main() {
    // if, else if, else example
    int a = 10, b = 20;

    std::cout << "if, else if, else example:\n";
    if (a > b) {
        std::cout << "a is greater than b\n";
    } else if (a < b) {
        std::cout << "a is less than b\n";
    } else {
        std::cout << "a is equal to b\n";
    }

    // switch statement example
    int day = 4; // Let's assume 1 = Monday, 2 = Tuesday, ..., 7 = Sunday

    std::cout << "\nswitch statement example:\n";
    switch (day) {
        case 1:
            std::cout << "Monday\n";
            break;
        case 2:
            std::cout << "Tuesday\n";
            break;
        case 3:
            std::cout << "Wednesday\n";
            break;
        case 4:
            std::cout << "Thursday\n";
            break;
        case 5:
            std::cout << "Friday\n";
            break;
        case 6:
            std::cout << "Saturday\n";
            break;
        case 7:
            std::cout << "Sunday\n";
            break;
        default:
            std::cout << "Invalid day\n";
    }

    // Nested if example
    std::cout << "\nNested if example:\n";
    int x = 30, y = 20;

    if (x == 30) {
        if (y == 20) {
            std::cout << "x is 30 and y is 20\n";
        }
    }

    return 0;
}
