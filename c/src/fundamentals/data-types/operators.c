#include <stdio.h>

int main() {
    // Arithmetic Operators
    int a = 10, b = 3;
    printf("Arithmetic Operators:\n");
    printf("a + b = %d\n", a + b);
    printf("a - b = %d\n", a - b);
    printf("a * b = %d\n", a * b);
    printf("a / b = %d\n", a / b); // Integer division
    printf("a %% b = %d\n", a % b);

    // Comparison Operators
    printf("\nComparison Operators:\n");
    printf("a == b: %d\n", a == b);
    printf("a != b: %d\n", a != b);
    printf("a > b: %d\n", a > b);
    printf("a < b: %d\n", a < b);
    printf("a >= b: %d\n", a >= b);
    printf("a <= b: %d\n", a <= b);

    // Assignment Operators
    printf("\nAssignment Operators:\n");
    a += b; // a = a + b;
    printf("a += b: %d\n", a);
    a -= b; // a = a - b;
    printf("a -= b: %d\n", a);
    // Other assignment operators include *=, /=, %=, <<=, >>=, &=, ^=, |=

    // Logical Operators
    int x = 1, y = 0; // In C, 1 is true and 0 is false
    printf("\nLogical Operators:\n");
    printf("x && y: %d\n", x && y);
    printf("x || y: %d\n", x || y);
    printf("!x: %d\n", !x);

    // Bitwise Operators
    int m = 5, n = 2; // 5 = 0101, 2 = 0010 in binary
    printf("\nBitwise Operators:\n");
    printf("m & n: %d\n", m & n);
    printf("m | n: %d\n", m | n);
    printf("m ^ n: %d\n", m ^ n);
    printf("~m: %d\n", ~m);
    printf("m << 1: %d\n", m << 1);
    printf("m >> 1: %d\n", m >> 1);

    // Increment/Decrement Operators
    int z = 0;
    printf("\nIncrement/Decrement Operators:\n");
    printf("z++: %d\n", z++); // Post-increment
    printf("++z: %d\n", ++z); // Pre-increment
    printf("z--: %d\n", z--); // Post-decrement
    printf("--z: %d\n", --z); // Pre-decrement

    return 0;
}
