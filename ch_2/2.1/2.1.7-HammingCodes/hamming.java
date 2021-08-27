/*
ID: alantao
LANG: JAVA
TASK: hamming
*/  

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.nio.file.Files;
import java.nio.file.Paths;

public class hamming {
  static StringTokenizer st;
  static int N, B, D;

  private static int getInt() {
    return Integer.parseInt(st.nextToken());
  }

  private static String booleanToString(boolean[] b) {
    int r = 0;
    for (int i = B - 1; i >= 0; i--) {
      r += b[i] ? Math.pow(2, B-i-1) : 0;
    }
    return Integer.toString(r);
  }

  private static int getHammingDistance(boolean[] b1, boolean[] b2) {
    int h = 0;
    for (int i = 0; i < B; i++) {
      if (b1[i] != b2[i]) {
        h++;
      }
    }
    return h;
  }

  private static boolean addOneToArr(boolean[] b) {
    int startingAt = -1;
    for (int i = B - 1; i >= 0; i--) {
      if (!b[i]) {
        b[i] = true;
        startingAt = i+1;
        break;
      }
    }

    if (startingAt == -1) {
      // already max
      return false;
    }

    for (int i = startingAt; i < B; i++) {
      b[i] = false;
    }

    return true;
  }

  private static List<boolean[]> getHammingDistanceNumbers() {
    boolean[] currentNum = new boolean[B];
    List<boolean[]> myNums = new ArrayList<>();
    int count = 0; 

    while (true) {
      if (count == N) {
        break;
      }

      boolean valid = true;
      for (boolean[] m: myNums) {
        if (getHammingDistance(m, currentNum) < D) {
          valid = false;
          break;
        }
      }

      if (valid) {
        myNums.add(currentNum);
        count++;
      }
      currentNum = currentNum.clone();
      if (!addOneToArr(currentNum)) {
        break;
      }
    }

    return myNums;
  }

  public static void main(String[] args) throws IOException{
    String in = new String(Files.readAllBytes(Paths.get("hamming.in")));
    st = new StringTokenizer(in);
    PrintWriter pw = new PrintWriter(new FileWriter("hamming.out"));

    N = getInt();
    B = getInt();
    D = getInt();

    int i = 0;
    List<boolean[]> myNums = getHammingDistanceNumbers();
    int myNumsSize = myNums.size();
    
    for (int j = 0; j < myNumsSize/10; j++) {
      for (int k = 0; k < 9; k++) {
        pw.print(booleanToString(myNums.get(i)) + " ");
        i++;
      }
      pw.println(booleanToString(myNums.get(i)));
      i++;
    }

    if (myNumsSize % 10 != 0) {
      for (int j = i; j < myNumsSize - 1; j++) {
        pw.print(booleanToString(myNums.get(i)) + " ");
        i++;
      }
      pw.print(booleanToString(myNums.get(i)));
    }

    if (myNumsSize % 10 != 0) {
      pw.println();
    }

    pw.close();
  }
}
