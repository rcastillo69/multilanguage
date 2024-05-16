#include <iostream>

using namespace std;

int sumInteger(int num1, int num2){
    return num1+num2;

}


int main() {
    
    int num1, num2;

    cin >> num1;
    cin >> num2;

    int sum = sumInteger(num1,num2);

    cout << sum;
    
    return 0;
}