/*
ID: alantao
LANG: JAVA
TASK: maze1
*/

import java.io.PrintWriter;
import java.io.StreamTokenizer;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;

public class maze1 {
  static StreamTokenizer st;
  static int W;
  static int H;
  static Cell[][] grid;

  public static void main(String[] args) throws Exception {
    // read input
    BufferedReader br = new BufferedReader(new FileReader("maze1.in"));
    // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    st = new StreamTokenizer(br);
    PrintWriter pw = new PrintWriter(new File("maze1.out"));
    // PrintWriter pw = new PrintWriter(System.out);
    String[] line_ = br.readLine().split(" ");
    W = Integer.parseInt(line_[0]);
    H = Integer.parseInt(line_[1]);

    grid = new Cell[H][W];

    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        grid[i][j] = new Cell();
      }
    }
    
    // solve
    int exit1I = -1;
    int exit1J = -1;
    int exit2I = -1;
    int exit2J = -1;
    for (int i = 0; i < H*2+1; i++) {
      char[] line = br.readLine().toCharArray();
      if (i%2==0) {
        // up down
        // assign down
        for (int j = 1; j < W*2+1; j+=2) {
          if (line[j] == '-') {
            if (i != 0) {
              grid[i/2-1][(j-1)/2].down = true;
            }
            if (i != H*2) {
              grid[i/2][(j-1)/2].up = true;
            }
          } else {
            if (i == 0) {
              if (exit1I == -1) {
                exit1I = 0;
                exit1J = (j-1)/2;
              } else {
                exit2I = 0;
                exit2J = (j-1)/2;
              }
              grid[0][(j-1)/2].up = true;
            } else if (i == H*2) {
              if (exit1I == -1) {
                exit1I = H-1;
                exit1J = (j-1)/2;
              } else {
                exit2I = H-1;
                exit2J = (j-1)/2;
              }
              grid[H-1][(j-1)/2].down = true;
            }
          }
        }
      } else {
        for (int j = 0; j < W*2+1; j+=2) {
          // assign right
          if (line[j] == '|') {
            if (j != 0) {
              grid[i/2][j/2-1].right = true;
            }
            if (j != W*2) {
              grid[i/2][j/2].left = true;
            }
          } else {
            if (j == 0) {
              if (exit1I == -1) {
                exit1I = i/2;
                exit1J = 0;
              } else {
                exit2I = i/2;
                exit2J = 0;
              }
              grid[i/2][0].left = true;
            } else if (j == W*2) {
              if (exit1I == -1) {
                exit1I = i/2;
                exit1J = W-1;
              } else {
                exit2I = i/2;
                exit2J = W-1;
              }
              grid[i/2][W-1].right = true;
            }
          }
        }
      }
    }

    Queue<Integer> q = new LinkedList<>();
    q.add(exit1I);
    q.add(exit1J);
    grid[exit1I][exit1J].visited = true;
    grid[exit1I][exit1J].distance = 1;
    recursive(1, q);

    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        grid[i][j].visited = false;
      }
    }

    q = new LinkedList<>();
    q.add(exit2I);
    q.add(exit2J);
    grid[exit2I][exit2J].visited = true;
    grid[exit2I][exit2J].distance = 1;
    recursive(1, q);

    int maxDistance = 1;
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        maxDistance = Math.max(maxDistance, grid[i][j].distance);
      }
    }

    pw.println(maxDistance);

    br.close();
    pw.close();
  }

  private static void recursive(int d, Queue<Integer> q) {
    if (q.isEmpty()) return;

    int size = q.size()/2;

    for (int k = 0; k < size; k++) {
      int i = q.poll();
      int j = q.poll();
      Cell cur = grid[i][j];
      if (!cur.up && !grid[i-1][j].visited) {
        grid[i-1][j].distance = Math.min(d+1,grid[i-1][j].distance);
        grid[i-1][j].visited = true;
        q.add(i-1);
        q.add(j);
      }
      if (!cur.down && !grid[i+1][j].visited) {
        grid[i+1][j].distance = Math.min(d+1, grid[i+1][j].distance);
        grid[i+1][j].visited = true;
        q.add(i+1);
        q.add(j);
      }
      if (!cur.left && !grid[i][j-1].visited) {
        grid[i][j-1].distance = Math.min(d+1, grid[i][j-1].distance);
        grid[i][j-1].visited = true;
        q.add(i);
        q.add(j-1);
      }
      if (!cur.right && !grid[i][j+1].visited) {
        grid[i][j+1].distance = Math.min(d+1, grid[i][j+1].distance);
        grid[i][j+1].visited = true;
        q.add(i);
        q.add(j+1);
      }
    }
    recursive(d+1, q);
  }

  private static class Cell {
    boolean up = false;
    boolean down = false;
    boolean left = false;
    boolean right = false;
    boolean visited = false;
    int distance = Integer.MAX_VALUE;

    @Override
    public String toString() {
      StringBuilder sb = new StringBuilder();
      sb.append(up?" - \n" : "   \n");
      sb.append(left? "| " : "  ");
      sb.append(right? "|\n" : " \n");
      sb.append(down? " - " : "   ");
      return sb.toString();
    }
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