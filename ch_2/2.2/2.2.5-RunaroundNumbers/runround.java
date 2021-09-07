/*
ID: alantao
LANG: JAVA
TASK: runround
*/

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.nio.file.Files;
import java.nio.file.Paths;

public class runround {
  static long M;
  static StringTokenizer st;

  private static long getLong() {
    return Long.parseLong(st.nextToken());
  }

  private static int addOne(int i, int l) {
    if (i == l - 1) {
      return 0;
    }
    return i + 1;
  }

  private static int getNextDigitIndex(long l, int i) {
    char[] lString = String.valueOf(l).toCharArray();
    int lStringLen = lString.length;

    int curIndex = i;
    for (int j = 0; j < lString[i] - '0'; j++) {
      curIndex = addOne(curIndex, lStringLen);
    }
    return curIndex;
  }

  private static boolean hasDistinctDigits(long number) {
    int numMask = 0;
    int numDigits = (int) Math.ceil(Math.log10(number+1));
    for (int digitIdx = 0; digitIdx < numDigits; digitIdx++) {
      int curDigit = (int)(number / Math.pow(10,digitIdx)) % 10;
      int digitMask = (int)Math.pow(2, curDigit);             
      if ((numMask & digitMask) > 0) return false;
      numMask = numMask | digitMask;
    }
    return true;
  }

  private static long getNexRunaroundNumber() {
    for (long curNum = M + 1; curNum < Long.MAX_VALUE; curNum++) {
      // check if curNum is runaround number
      if (!String.valueOf(curNum).contains("0") && hasDistinctDigits(curNum)) {
        int digitIndex = 0;
        int count = 0;
        boolean[] visited = new boolean[(int)(Math.log10(curNum)+1)];
        while (true) {
          visited[digitIndex] = true;
          count++;
          digitIndex = getNextDigitIndex(curNum, digitIndex);
          if (visited[digitIndex]) {
            if (count == visited.length && digitIndex == 0) {
              // valid
              return curNum;
            }
            // not valid
            break;
          }
        }
      }
    }
    return 0;
  }

  public static void main(String[] args) throws IOException{
    String in = new String(Files.readAllBytes(Paths.get("runround.in")));
    st = new StringTokenizer(in);
    PrintWriter pw = new PrintWriter(new FileWriter("runround.out"));

    M = getLong();
 
    pw.println(getNexRunaroundNumber());

    pw.close();
  }

}