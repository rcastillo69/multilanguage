#include <iostream>

int main() {
    // while loop example
    int i = 0;
    std::cout << "while loop:\n";
    while (i < 5) {
        std::cout << i << " ";
        i++;
    }

    std::cout << "\n\nfor loop:\n";
    // for loop example
    for (int j = 0; j < 5; j++) {
        std::cout << j << " ";
    }

    std::cout << "\n\ndo-while loop:\n";
    // do-while loop example
    int k = 0;
    do {
        std::cout << k << " ";
        k++;
    } while (k < 5);

    std::cout << "\n\ncontinue in loop:\n";
    // continue example
    for (int l = 0; l < 5; l++) {
        if (l == 2) continue;
        std::cout << l << " ";
    }

    std::cout << "\n\nbreak in loop:\n";
    // break example
    for (int m = 0; m < 5; m++) {
        if (m == 3) break;
        std::cout << m << " ";
    }

    std::cout << "\n\nnested loops with break:\n";
    // nested loops with break
    for (int n = 0; n < 3; n++) {
        for (int o = 0; o < 3; o++) {
            if (o == 1) break;
            std::cout << "n=" << n << ", o=" << o << "; ";
        }
    }

    std::cout << "\n\nbreaking out of all nested loops:\n";
    // breaking out of all nested loops
    bool stop = false;
    for (int p = 0; p < 3 && !stop; p++) {
        for (int q = 0; q < 3; q++) {
            if (q == 1) {
                stop = true;
                break;
            }
            std::cout << "p=" << p << ", q=" << q << "; ";
        }
    }

    return 0;
}
