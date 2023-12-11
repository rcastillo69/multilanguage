#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    // char to int, float
    char ch = '5';
    int charToInt = ch - '0'; // Convert char to int
    float charToFloat = (float)charToInt; // Convert int to float

    printf("char to int: %d\n", charToInt);
    printf("char to float: %f\n", charToFloat);

    // string (char array) to int, float
    char str[] = "123";
    int stringToInt = atoi(str); // Convert string to int
    float stringToFloat = atof(str); // Convert string to float

    printf("string to int: %d\n", stringToInt);
    printf("string to float: %f\n", stringToFloat);

    // int to float, double
    int num = 42;
    float intToFloat = (float)num; // Convert int to float
    double intToDouble = (double)num; // Convert int to double

    printf("int to float: %f\n", intToFloat);
    printf("int to double: %f\n", intToDouble);

    return 0;
}
