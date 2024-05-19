#include <iostream>

bool isDivisibilityBy(int number, int div_by){
    return number % div_by == 0;
}

bool isLeap(int yearInput){
    return isDivisibilityBy(yearInput, 4) &&
           (!isDivisibilityBy(yearInput, 100) || isDivisibilityBy(yearInput, 400));
}

int main(){
    int year;
    std::cout << "Enter year: ";
    std::cin >> year;

    std::cout << (isLeap(year) ? "true" : "false") << std::endl;

    return 0;
}
