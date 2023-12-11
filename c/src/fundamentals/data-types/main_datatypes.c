#include <stdio.h>
#include <stdbool.h>
#include <time.h>

// Enumeration type
enum DayOfWeek { Sun, Mon, Tue, Wed, Thu, Fri, Sat };

int main() {
    // Integer type
    int myInt = 10;
    printf("Integer: %d\n", myInt);

    // Floating point type
    float myFloat = 3.14;
    printf("Float: %f\n", myFloat);

    // Double type
    double myDouble = 9.82;
    printf("Double: %lf\n", myDouble);

    // Character type
    char myChar = 'A';
    printf("Character: %c\n", myChar);

    // Boolean type (using stdbool.h)
    bool myBool = true;
    printf("Boolean: %s\n", myBool ? "true" : "false");

    // Long type
    long myLong = 123456789L;
    printf("Long: %ld\n", myLong);

    // Long long type
    long long myLongLong = 123456789012345LL;
    printf("Long long: %lld\n", myLongLong);

    // Unsigned int
    unsigned int myUnsignedInt = 3000000000U;
    printf("Unsigned Integer: %u\n", myUnsignedInt);

    // Short type
    short myShort = 32767;
    printf("Short: %hd\n", myShort);

    // Constant type
    const int myConstInt = 42;
    printf("Constant Integer: %d\n", myConstInt);

    // Date and time
    time_t now;
    time(&now);
    struct tm *local = localtime(&now);

    printf("Date and Time: %d-%d-%d %d:%d:%d\n", 
            local->tm_year + 1900, local->tm_mon + 1, local->tm_mday,
            local->tm_hour, local->tm_min, local->tm_sec);

    // Pointer type
    int* ptr = &myInt;
    printf("Pointer: %p\n", (void*)ptr);

   // Enum type
    enum DayOfWeek today = Wed;
    printf("Enum (Day of Week): %d\n", today);


    return 0;

}
