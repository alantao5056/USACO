/*
ID: alantao
TASK: prefix
LANG: C++14
*/

#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> choices;
vector<bool> dp(200001);
string mainStr;
int N;

int solve() {
  for (int i = 0; i < N; i++) {
    if (!dp[i]) {
      continue;
    }

    for (string choice : choices) {
      // compare choice to mainStr
      bool fits = true;
      for (int j = i; j < i + choice.length(); j++) {
        if (j > N) {
          // index out of range
          fits = false;
          break;
        }
        if (choice[j-i] != mainStr[j]) {
          // not the same
          fits = false;
          break;
        }
      }

      if (fits) {
        dp[i + choice.length()] = true;
      }
    }
  }

  // get first true from dp
  for (int i = N; i >= 0; i--) {
    if (dp[i]) {
      // found
      return i;
    }
  }
  return 0;
}

int main() {
  freopen("prefix.in", "r", stdin);
  freopen("prefix.out", "w", stdout);

  string cur;
  cin >> cur;

  // get the choices
  while (cur != ".") {
    choices.push_back(cur);
    // cout << cur << endl;
    cin >> cur;
  }

  // get the string
  while (cin >> cur) {
    mainStr += cur;
  }

  N = mainStr.length();
  dp[0] = true;

  // print
  cout << solve() << endl;

  return 0;
}