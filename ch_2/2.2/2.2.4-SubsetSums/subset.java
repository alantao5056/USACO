/*
ID: alantao
LANG: JAVA
TASK: subset
*/

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.nio.file.Files;
import java.nio.file.Paths;

public class subset {
  static int N;
  static StringTokenizer st;

  private static int getInt() {
    return Integer.parseInt(st.nextToken());
  }

  private static long getNumberOfSubsets() {
    final int TOTAL = (N + 1)*N/2;
    
    if (TOTAL % 2 != 0) {
      return 0;
    }

    final int ADDUP_NUMBER = TOTAL/2;

    long[] arr = new long[ADDUP_NUMBER + 1];

    // one way to make 1
    arr[1] = 1;

    for (int curAdding = 2; curAdding <= N; curAdding++) {
      System.out.println(Arrays.toString(arr));
      for (int i = ADDUP_NUMBER; i >= 1; i--) {
        // adding curAdding to i
        if (curAdding + i <= ADDUP_NUMBER && arr[i] > 0) {
          arr[curAdding + i] += arr[i];
        }
      }

      arr[curAdding]++;
    }

    System.out.println(Arrays.toString(arr));
    return arr[ADDUP_NUMBER]/2;
  }

  
  public static void main(String[] args) throws IOException {
    String in = new String(Files.readAllBytes(Paths.get("subset.in")));
    st = new StringTokenizer(in);
    PrintWriter pw = new PrintWriter(new FileWriter("subset.out"));

    N = getInt();
 
    pw.println(getNumberOfSubsets());

    pw.close();
  }
}