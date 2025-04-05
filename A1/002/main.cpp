#include <iostream>
using namespace std;

int main(){
    int amount;
    cin >> amount;
    int c10 = amount / 10; amount %= 10;
    int c5 = amount / 5; amount %= 5;
    int c2 = amount / 2; amount %= 2;
    int c1 = amount;
    cout << "10 = " << c10 << "\n";
    cout << "5 = " << c5 << "\n";
    cout << "2 = " << c2 << "\n";
    cout << "1 = " << c1 << "\n";
    return 0;
}
