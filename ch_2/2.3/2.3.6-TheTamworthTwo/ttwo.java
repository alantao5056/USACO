/*
ID: alantao
LANG: JAVA
TASK: ttwo
*/

import java.io.PrintWriter;
import java.io.StreamTokenizer;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;

class ttwo {
  static StreamTokenizer st;
  static char[][] grid = new char[12][12];
  static int[] i_ = {-1, 0, 1, 0};
  static int[] j_ = {0, 1, 0, -1};


  public static void main(String[] args) throws Exception {
    // read input
    BufferedReader br = new BufferedReader(new FileReader("ttwo.in"));
    // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    st = new StreamTokenizer(br);
    PrintWriter pw = new PrintWriter(new File("ttwo.out"));
    // PrintWriter pw = new PrintWriter(System.out);
    
    // solve
    for (int i = 0; i < 12; i++) {
      grid[0][i] = '*';
      grid[11][i] = '*';
    }

    for (int i = 1; i < 11; i++) {
      grid[i][0] = '*';
      grid[i][11] = '*';
    }


    int cowI = 0;
    int cowJ = 0;
    int farmerI = 0;
    int farmerJ = 0;

    for (int i = 1; i <= 10; i++) {
      char[] line = br.readLine().toCharArray();

      for (int j = 1; j <= 10; j++) {
        if (line[j-1] == 'C') {
          cowI = i;
          cowJ = j;
          line[j-1] = '.';
        } else if (line[j-1] == 'F') {
          farmerI = i;
          farmerJ = j;
          line[j-1] = '.';
        }
        grid[i][j] = line[j-1];
      }
    }

    int cowDirection = 0;
    int farmerDirection = 0;
    int count = 0;

    while (count < 160001 && (cowI != farmerI || cowJ != farmerJ)) {
      // move cow
      int cowNextI = cowI + i_[cowDirection];
      int cowNextJ = cowJ + j_[cowDirection];
      if (grid[cowNextI][cowNextJ] == '*') {
        cowDirection++;
        cowDirection %= 4;
      } else {
        cowI = cowNextI;
        cowJ = cowNextJ;
      }

      // move farmer
      int farmerNextI = farmerI + i_[farmerDirection];
      int farmerNextJ = farmerJ + j_[farmerDirection];
      if (grid[farmerNextI][farmerNextJ] == '*') {
        farmerDirection++;
        farmerDirection %= 4;
      } else {
        farmerI = farmerNextI;
        farmerJ = farmerNextJ;
      }

      count++;
    }

    if (count <= 160000) {
      pw.println(count);
    } else {
      pw.println(0);
    }

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