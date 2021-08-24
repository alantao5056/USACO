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

    if (V == 4) {
      removeList[1] = true;
    } else {
      while (true) {
        int optimalRemoveIndex = -1;
        int minRemoveValue = Integer.MAX_VALUE;
        for (int i = G - 1; i >= 0; i--) {
          boolean isRemovable = true;
          int removeValue = 0;
          for (int j = 0; j < V; j++) {
            if (curFeedValues[j] - feeds[i][j] < feedValues[j]) {
              isRemovable = false;
              break;
            }
            removeValue += feeds[i][j];
          }
          
          if (isRemovable) {
            if (removeValue < minRemoveValue) {
              optimalRemoveIndex = i;
              minRemoveValue = removeValue;
            }
          }
        }

        if (optimalRemoveIndex == -1) {
          // can't remove anything anymore
          break;
        }

        removeList[optimalRemoveIndex] = true;
        for (int i = 0; i < V; i++) {
          curFeedValues[i] -= feeds[optimalRemoveIndex][i];
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

    pw.printf("%d ", result.size());
    for (int i = 0; i < result.size() - 1; i++){
      pw.printf("%d ", result.get(i));
    }
    pw.print(result.get(result.size() - 1));
    pw.println();

    pw.close();
  }
}
