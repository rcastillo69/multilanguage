#include <stdio.h>

int main() {
    // if, else if, else example
    int a = 10, b = 20;

    printf("if, else if, else example:\n");
    if (a > b) {
        printf("a is greater than b\n");
    } else if (a < b) {
        printf("a is less than b\n");
    } else {
        printf("a is equal to b\n");
    }

    // switch statement example
    int day = 4; // Let's assume 1 = Monday, 2 = Tuesday, ..., 7 = Sunday

    printf("\nswitch statement example:\n");
    switch (day) {
        case 1:
            printf("Monday\n");
            break;
        case 2:
            printf("Tuesday\n");
            break;
        case 3:
            printf("Wednesday\n");
            break;
        case 4:
            printf("Thursday\n");
            break;
        case 5:
            printf("Friday\n");
            break;
        case 6:
            printf("Saturday\n");
            break;
        case 7:
            printf("Sunday\n");
            break;
        default:
            printf("Invalid day\n");
    }

    // Nested if example
    printf("\nNested if example:\n");
    int x = 30, y = 20;

    if (x == 30) {
        if (y == 20) {
            printf("x is 30 and y is 20\n");
        }
    }

    return 0;
}
