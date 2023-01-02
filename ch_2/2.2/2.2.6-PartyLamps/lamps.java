/*
ID: alantao
LANG: JAVA
TASK: lamps
*/

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Collections;


public class lamps {
  static int N;
  static int C;
  static StringTokenizer st;
  static List<Integer> on = new ArrayList<>();
  static List<Integer> off = new ArrayList<>();

  private static int getInt() {
    return Integer.parseInt(st.nextToken());
  }

  private static void addOne(boolean[] s) {
    for (int i = 3; i > -1; i--) {
      if (!s[i]) {
        s[i] = true;
        // zero
        for (int j = i + 1; j < 4; j++) {
          s[j] = false;
        }
        break;
      }
    }
  }

  private static boolean[] pressButton(boolean[] s) {
    boolean[] result = new boolean[N];
    Arrays.fill(result, true);
    if (s[0]) {
      // first button
      for (int i = 0; i < N; i++) {
        result[i] = !result[i];
      }
    }
    if (s[1]) {
      // second button
      for (int i = 0; i < N; i+=2) {
        result[i] = !result[i];
      }
    }
    if (s[2]) {
      // thrid button
      for (int i = 1; i < N; i+=2) {
        result[i] = !result[i];
      }
    }
    if (s[3]) {
      // fourth button
      for (int i = 0; i < N; i += 3) {
        result[i] = !result[i];
      }
    }
    return result;
  }

  private static List<boolean[]> solve() {
    List<boolean[]> result = new ArrayList<>();
    boolean[] binary = new boolean[4];

    for (int i = 0; i < 16; i++) {
      boolean[] afterPresses = pressButton(binary);
      int numberOfPresses = 0;
      for (int j = 0; j < 4; j++) {
        numberOfPresses += binary[j] ? 1 : 0;
      }
      
      // VALID TEST
      if (numberOfPresses <= C && (C - numberOfPresses) % 2 == 0) {
        // number of presses is valid
        // testing if restrictions are valid
        boolean valid = true;
        for (int o : on) {
          if (!afterPresses[o]) {
            // not valid
            valid = false;
            break;
          }
        }
        for (int o : off) {
          if (afterPresses[o]) {
            // not valid
            valid = false;
            break;
          }
        }
        
        if (valid) {
          result.add(afterPresses);
        }
      }
      addOne(binary);
    }

    return result;
  }

  public static void main(String[] args) throws IOException{
    String fileInput = new String(Files.readAllBytes(Paths.get("lamps.in")));
    PrintWriter pw = new PrintWriter(new FileWriter("lamps.out"));
    st = new StringTokenizer(fileInput);
    
    N = getInt();
    C = getInt();

    int curGetInt = getInt();
    while (curGetInt != -1) {
      on.add(curGetInt - 1);
      curGetInt = getInt();
    }

    curGetInt = getInt();
    while (curGetInt != -1) {
      off.add(curGetInt - 1);
      curGetInt = getInt();
    }

    List<boolean[]> resultList = solve();

    Collections.sort(resultList, new Comparator<boolean[]>() {
      @Override
      public int compare(boolean[] o1, boolean[] o2) {
        for (int i = 0; i < N; i++) {
          if (o1[i]) {
            if (!o2[i]) {
              // o1 > o2
              return 0;
            }
          } else {
            if (o2[i]) {
              // o2 > o1
              return -1;
            }
          }
        }
        return 1;
      }
    });

    if (resultList.size() == 0) {
      pw.println("IMPOSSIBLE");
    } else {
      for (boolean[] r: resultList) {
        char[] charArr = new char[N];
        for (int i = 0; i < N; i++) {
          charArr[i] = r[i] ? '1' : '0';
        }

        String r2 = new String(charArr);

        pw.println(r2);
      }
    }

    pw.close();
  }
}