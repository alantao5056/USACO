/*
ID: alantao
LANG: JAVA
TASK: money
*/

import java.io.PrintWriter;
import java.io.StreamTokenizer;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;

class money {
  static StreamTokenizer st;
  static int V;
  static int N;

  public static void main(String[] args) throws Exception {
    // read input
    BufferedReader br = new BufferedReader(new FileReader("money.in"));
    // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    st = new StreamTokenizer(br);
    PrintWriter pw = new PrintWriter(new File("money.out"));
    // PrintWriter pw = new PrintWriter(System.out);
    V = nextInt();
    N = nextInt();
    
    // solve
    long[] dp = new long[10001];
    dp[0] = 1;
    for (int i = 0; i < V; i++) {
      int coin = nextInt();

      for (int j = coin; j < 10001; j++) {
        dp[j] += dp[j-coin];
      }
    }

    pw.println(dp[N]);

    br.close();
    pw.close();
  }

  private static int nextInt() throws Exception {
    st.nextToken();
    return (int) st.nval;
  }

  private static String nextString() throws Exception {
    st.nextToken();
    return st.sval;
  }
}