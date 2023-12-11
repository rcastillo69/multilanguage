#include <stdio.h>
#include <stdbool.h>

int main() {
    // while loop example
    int i = 0;
    printf("while loop:\n");
    while (i < 5) {
        printf("%d ", i);
        i++;
    }

    printf("\n\nfor loop:\n");
    // for loop example
    for (int j = 0; j < 5; j++) {
        printf("%d ", j);
    }

    printf("\n\ndo-while loop:\n");
    // do-while loop example
    int k = 0;
    do {
        printf("%d ", k);
        k++;
    } while (k < 5);

    printf("\n\ncontinue in loop:\n");
    // continue example
    for (int l = 0; l < 5; l++) {
        if (l == 2) continue;
        printf("%d ", l);
    }

    printf("\n\nbreak in loop:\n");
    // break example
    for (int m = 0; m < 5; m++) {
        if (m == 3) break;
        printf("%d ", m);
    }

    printf("\n\nnested loops with break:\n");
    // nested loops with break
    for (int n = 0; n < 3; n++) {
        for (int o = 0; o < 3; o++) {
            if (o == 1) break;
            printf("n=%d, o=%d; ", n, o);
        }
    }

    printf("\n\nbreaking out of all nested loops:\n");
    // breaking out of all nested loops
    bool stop = false;
    for (int p = 0; p < 3 && !stop; p++) {
        for (int q = 0; q < 3; q++) {
            if (q == 1) {
                stop = true;
                break;
            }
            printf("p=%d, q=%d; ", p, q);
        }
    }

    return 0;
}
