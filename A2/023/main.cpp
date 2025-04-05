#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    getline(cin, s);
    int n = (int)s.size();
    bool allIT = true;
    for(int i = 0; i < n; i++){
        char c = toupper(s[i]);
        if(c != 'I' && c != 'T'){
            allIT = false;
            break;
        }
    }
    if(allIT){
        cout << "unknown " << n;
        return 0;
    }
    int maxA = 0;
    for(int i = 0; i < n; i++){
        char c = toupper(s[i]);
        if(c == 'R'){
            if(i == n - 1 || toupper(s[i + 1]) != 'A'){
                cout << "no " << (i == n - 1 ? i : i + 1);
                return 0;
            }
            int countA = 0, j = i + 1;
            while(j < n && toupper(s[j]) == 'A'){
                countA++;
                j++;
            }
            maxA = max(maxA, countA);
            i = j - 1;
        }
        else if(c == 'A'){
            if(i == 0 || toupper(s[i - 1]) != 'R'){
                cout << "no " << i;
                return 0;
            }
        }
        else if(c == 'B'){
            if(i == n - 1 || (toupper(s[i + 1]) != 'I' && toupper(s[i + 1]) != 'T')){
                cout << "no " << (i == n - 1 ? i : i + 1);
                return 0;
            }
            int j = i + 1;
            while(j < n && (toupper(s[j]) == 'I' || toupper(s[j]) == 'T')){
                j++;
            }
            i = j - 1;
        }
        else if(c == 'I' || c == 'T'){
        }
        else {
            cout << "no " << i;
            return 0;
        }
    }
    cout << "yes " << maxA;
    return 0;
}
