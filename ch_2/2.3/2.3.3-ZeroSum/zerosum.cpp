/*
ID: alantao
LANG: C++14
TASK: zerosum
*/

#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int N;

int intToChar(int i) {
  return '0' + i;
}

void addOne(string & s) {
  int changeIndex = -1;
  // ' ' '+' '-'
  for (int i = N - 2; i >= 0; i--) {
    if (s[i] != '-') {
      if (s[i] == '+') {
        s[i] = '-';
        changeIndex = i + 1;
        break;
      } else {
        // s[i] is ' '
        s[i] = '+';
        changeIndex = i + 1;
        break;
      }
    }
  }

  // replace 2's with 0's
  for (int i = changeIndex; i < N - 1; i++) {
    s[i] = ' ';
  }
}

int main() {
  freopen("zerosum.in", "r", stdin);
  freopen("zerosum.out", "w", stdout);

  cin >> N;

  string comb(N - 1, ' ');

  for (int i = 0; i < pow(3, N - 1); i++) {
    // making formattedString
    string formattedString(N * 2 - 1, ' ');
    int formattedStringIndex = 0;
    for (int j = 1; j < N; j++) {
      // number
      formattedString[formattedStringIndex] = intToChar(j);
      // operation
      formattedString[formattedStringIndex + 1] = comb[j - 1];
      formattedStringIndex += 2;
    }
    formattedString[formattedStringIndex] = intToChar(N);

    // start calculating
    int combCurIndex = 0;
    int result = 0;
    int currentValue = 0;
    int currentOperation = '+';

    for (int j = 0; j < N * 2 - 1; j++) {
      char curChar = formattedString[j];
      if (curChar == ' ') { continue; }
      if (curChar == '+' || curChar == '-') {
        // operation
        if (currentOperation == '+') {
          result += currentValue;
        } else {
          // currentOperation == '-'
          result -= currentValue;
        }

        if (curChar != ' ') {
          currentValue = 0;
          currentOperation = curChar;
        }
      } else {
        // number
        int intCurChar = curChar - '0';
        currentValue *= 10;
        currentValue += intCurChar;
      }
    }
    // do operation again
    if (currentOperation == '+') {
      result += currentValue;
    } else {
      // currentOperation = '-'
      result -= currentValue;
    }

    // printing results
    if (result == 0) {
      cout << formattedString << endl;
    }

    addOne(comb);
  }

  return 0;
}