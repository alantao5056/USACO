/*
ID: alantao
TASK: nocows
LANG: C++14
*/

#include <iostream>
using namespace std;

int N, K;
unsigned long long dp[210][110];

int main() {
  freopen("nocows.in", "r", stdin);
  freopen("nocows.out", "w", stdout);

  cin >> N >> K;

  for (int i = 1; i < N + 1; i+=2) {
    for (int j = 1; j < K + 1; j++) {
      if (i == 1) {
        dp[i][j] = 1;
      } else {
        for (int k = 1; k < i-1; k+=2) {
          dp[i][j] += dp[k][j-1] * dp[i-k-1][j-1];
          dp[i][j] %= 9901;
        }
      }
    }
  }

  cout << (dp[N][K] - dp[N][K-1] + 9901)%9901 << endl;

  return 0;
}