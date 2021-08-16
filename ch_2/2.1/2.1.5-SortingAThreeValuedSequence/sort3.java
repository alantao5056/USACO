/*
ID: alantao
LANG: JAVA
TASK: sort3
*/


import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.nio.file.Files;
import java.nio.file.Paths;

public class sort3 {
  static int N;
  static int[] myArr;
  static StringTokenizer st;

  private static int getInt() {
    return Integer.parseInt(st.nextToken());
  }

  private static void swap(int a, int b) {
    int temp = myArr[a];
    myArr[a] = myArr[b];
    myArr[b] = temp;
  }

  public static void main(String[] args) throws IOException{
    String in = new String(Files.readAllBytes(Paths.get("sort3.in")));
    st = new StringTokenizer(in);
    PrintWriter pw = new PrintWriter(new FileWriter("sort3.out"));

    N = getInt();

    // init myArr
    myArr = new int[N];
    int oneEnd = 0;
    int twoEnd = 0;

    for (int i = 0; i < N; i++) {
      int curInt = getInt();
      myArr[i] = curInt;
      if (curInt == 1) oneEnd++;
      else if (curInt == 2) twoEnd++;
    }
    twoEnd += oneEnd;

    int swaps = 0;
    // start swapping 1s
    int curTarget;
    for (int i = 0; i < oneEnd; i++) {
      curTarget = myArr[i];

      int curSwapTarget;
      if (curTarget != 1) {
        // target needs swap
        if (curTarget == 2) {
          for (int j = i+1; j < N; j++) {
            curSwapTarget = myArr[j];
            if (curSwapTarget == 1) {
              // check if swap target is already in place
              if (j >= oneEnd) {
                // swap
                swap(i, j);
                swaps++;
                break;
              }
            }
          }
        } else {
          // it's a three
          for (int j = N - 1; j > i; j--) {
            curSwapTarget = myArr[j];
            if (curSwapTarget == 1) {
              // check if swap target is already in place
              if (j >= oneEnd) {
                // swap
                swap(i, j);
                swaps++;
                break;
              }
            }
          }
        }
        
      }
    }

    // start swapping 2s
    for (int i = oneEnd; i < twoEnd; i++) {
      curTarget = myArr[i];

      int curSwapTarget;
      if (curTarget != 2) {
        // target needs swap
        for (int j = i+1; j < N; j++) {
          curSwapTarget = myArr[j];
          if (curSwapTarget == 2) {
            // check if swap target is already in place
            if (j >= twoEnd) {
              // swap
              swap(i, j);
              swaps++;
              break;
            }
          }
        }
      }
    }

    pw.println(swaps);

    pw.close();
  }
}