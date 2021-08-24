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

  private static List<Integer> getFeeds() {
    // initializing curFeedValues
    int[] curFeedValues = new int[V];
    for (int i = 0; i < G; i++) {
      for (int j = 0; j < V; j++) {
        curFeedValues[j] += feeds[i][j];
      }
    }

    // check the biggest to remove
    boolean[] removeList = new boolean[G];
    for (int i = G - 1; i >= 0; i--) {
      boolean isRemovable = true;
      for (int j = 0; j < V; j++) {
        if (curFeedValues[j] - feeds[i][j] < feedValues[j]) {
          isRemovable = false;
          break;
        }
      }
      
      if (isRemovable) {
        removeList[i] = true;
        for (int j = 0; j < V; j++) {
          curFeedValues[j] -= feeds[i][j];
        }
      }
    }

    // generate list
    List<Integer> result = new ArrayList<>();
    for (int i = 0; i < G; i++) {
      if (!removeList[i]) {
        result.add(i + 1);
      }
    }

    return result;
  }

  private static List<Integer> getFeeds2() {
    // initializing curFeedValues
    int[] curFeedValues = new int[V];
    for (int i = 0; i < G; i++) {
      for (int j = 0; j < V; j++) {
        curFeedValues[j] += feeds[i][j];
      }
    }

    // check the biggest to remove
    boolean[] removeList = new boolean[G];
    for (int i = 0; i < G; i++) {
      boolean isRemovable = true;
      for (int j = 0; j < V; j++) {
        if (curFeedValues[j] - feeds[i][j] < feedValues[j]) {
          isRemovable = false;
          break;
        }
      }
      
      if (isRemovable) {
        removeList[i] = true;
        for (int j = 0; j < V; j++) {
          curFeedValues[j] -= feeds[i][j];
        }
      }
    }

    // generate list
    List<Integer> result = new ArrayList<>();
    for (int i = 0; i < G; i++) {
      if (!removeList[i]) {
        result.add(i + 1);
      }
    }

    return result;
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
    List<Integer> result2 = getFeeds2();
    List<Integer> actualResult = result;

    // compare result and result2

    if (result.size() < result2.size()) {
      actualResult = result;
    } else if (result.size() > result2.size()) {
      actualResult = result2;
    } else {
      for (int i = 0; i < Math.min(result.size(), result2.size()); i++) {
        if (result.get(i) < result2.get(i)) {
          actualResult = result;
        }
        if (result.get(i) > result2.get(i)) {
          actualResult = result2;
        }
      }
    }

    pw.printf("%d ", actualResult.size());
    for (int i = 0; i < actualResult.size() - 1; i++){
      pw.printf("%d ", actualResult.get(i));
    }
    pw.print(actualResult.get(actualResult.size() - 1));
    pw.println();

    pw.close();
  }
}
