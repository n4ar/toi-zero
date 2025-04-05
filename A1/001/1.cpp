#include <iostream>
#include <string>
using namespace std;

int main() {
    string name, surname;
    cout << "กรุณากรอกชื่อ: ";
    getline(cin, name);
    cout << "กรุณากรอกนามสกุล: ";
    getline(cin, surname);
    string first_two_name = name.substr(0, 2);
    string combined_surname_part;
    if (surname.substr(0, 2) == first_two_name) {
        if (surname.length() > 2)
            combined_surname_part = surname.substr(2, 2);
        else
            combined_surname_part = "";
    } else {
        combined_surname_part = surname.substr(0, 2);
    }
    string new_word = first_two_name + combined_surname_part;
    cout << "Hello " << name << " " << surname << "\n";
    cout << new_word << "\n";
    return 0;
}
