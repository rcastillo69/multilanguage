#include <stab.h>

int main() {
    float temperature_frn = 0;

    printf("Please enter a temperature value in Farenheit!\n");

    scanf("%f", &temperature_frn);

    float temperature_clc = (temperature_frn - 32) * 5 / 9;

    printf("The temperature in Celsius is %.2f\n", temperature_clc);

    return 0;
}