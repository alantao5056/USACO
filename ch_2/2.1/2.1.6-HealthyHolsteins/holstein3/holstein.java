/*
ID: alantao
LANG: JAVA
TASK: holstein
*/  

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.nio.file.Files;
import java.nio.file.Paths;

public class holstein {
  static StringTokenizer st;
  static int V;
  static int G;
  static int[] feedValues;
  static int[][] feeds;

  private static int getInt() {
    return Integer.parseInt(st.nextToken());
  }

  private static String fillLeftWithZeros(String s, int size) {
    if (s.length() < size) {
      String zeros = new String(new char[size - s.length()]).replace('\0', '0');
      return zeros.concat(s);
    }
    return s;
  }

  private static int countOnes(String s) {
    int count = 0;
    for (char c : s.toCharArray()) {
      if (c == '1') {
        count++;
      }
    }
    return count;
  }

  private static int compare(String a, String b) {
    for (int i = 0; i < G; i++) {
      if (a.charAt(i) != b.charAt(i)) {
        if (a.charAt(i) == '1') {
          return 0;
        } else {
          return 1;
        }
      }
    }
    return -1;
  }

  private static List<Integer> getFeeds() {
    int minLength = Integer.MAX_VALUE;
    List<String> validCombs = new ArrayList<>();

    // get valids
    for (int i = 0; i < Math.pow(2, G); i++) {
      String binary = fillLeftWithZeros(Integer.toBinaryString(i), G);
      boolean isValid = true;
      for (int j = 0; j < V; j++) {
        int rowCount = 0;
        for (int k = 0; k < G; k++) {
          if (binary.charAt(k) == '1') {
            rowCount += feeds[k][j];
          }
        }

        if (rowCount < feedValues[j]) {
          // doesn't work
          isValid = false;
          break;
        }
      }

      if (isValid) {
        validCombs.add(binary);
        minLength = Math.min(countOnes(binary), minLength);
      }
    }

    // filter validCombs
    List<String> sameLengthCombs = new ArrayList<>();
    for (String v : validCombs) {
      if (countOnes(v) == minLength) {
        sameLengthCombs.add(v);
      }
    }

    // filter sameLengthCombs
    String result = new String();
    for (int i = 0; i < sameLengthCombs.size() - 1; i++) {
      int compareResult = compare(sameLengthCombs.get(i), sameLengthCombs.get(i+1));
      if (compareResult == 1) {
        result = sameLengthCombs.get(i+1);
      } else {
        result = sameLengthCombs.get(i);
      }
    }
    if (sameLengthCombs.size() == 1) {
      result = sameLengthCombs.get(0);
    }

    // result tostring
    List<Integer> toStringResult = new ArrayList<>();

    for (int i = 0; i < G; i++) {
      if (result.charAt(i) == '1') {
        toStringResult.add(i + 1);
      }
    }

    return toStringResult;

  }

  public static void main(String[] args) throws IOException{
    String in = new String(Files.readAllBytes(Paths.get("holstein.in")));
    st = new StringTokenizer(in);
    PrintWriter pw = new PrintWriter(new FileWriter("holstein.out"));

    V = getInt();
    feedValues = new int[V];
    for (int i = 0; i < V; i++) {
      feedValues[i] = getInt();
    }

    G = getInt();
    feeds = new int[G][V];
    for (int i = 0; i < G; i++) {
      for (int j = 0; j < V; j++) {
        feeds[i][j] = getInt();
      }
    }

    List<Integer> result = getFeeds();

    pw.printf("%d ", result.size());
    for (int i = 0; i < result.size() - 1; i++){
      pw.printf("%d ", result.get(i));
    }
    pw.print(result.get(result.size() - 1));
    pw.println();

    pw.close();
  }
}
