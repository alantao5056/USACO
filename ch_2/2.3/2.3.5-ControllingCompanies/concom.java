/*
ID: alantao
LANG: JAVA
TASK: concom
*/

import java.io.PrintWriter;
import java.io.StreamTokenizer;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;

class concom {
  static StreamTokenizer st;
  static int N;
  static Comp[] companies;

  public static void main(String[] args) throws Exception {
    // read input
    BufferedReader br = new BufferedReader(new FileReader("concom.in"));
    // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    st = new StreamTokenizer(br);
    PrintWriter pw = new PrintWriter(new File("concom.out"));
    // PrintWriter pw = new PrintWriter(System.out);
    
    // solve
    companies = new Comp[101];
    for (int i = 0; i < 101; i++) {
      companies[i] = new Comp(i);
    }
    N = nextInt();

    for (int i = 0; i < N; i++) {
      int a = nextInt()-1;
      int b = nextInt()-1;
      int value = nextInt();

      companies[a].add(b, value);
    }

    for (int i = 0; i < 101; i++) {
      int[] percents = new int[101];
      boolean[] visited = new boolean[101];
      ArrayDeque<Comp> comps = new ArrayDeque<>();
      comps.add(companies[i]);
      visited[i] = true;
      while (!comps.isEmpty()) {
        Comp cur = comps.poll();

        for (int j = 0; j < cur.nbs.size(); j++) {
          Comp nb = cur.nbs.get(j);
          percents[nb.id] += cur.values.get(j);
          if (!visited[nb.id] && percents[nb.id] > 50) {
            comps.add(nb);
            visited[nb.id] = true;
          }
        }
      }

      for (int j = 0; j < 101; j++) {
        if (j!=i && percents[j] > 50) {
          pw.print(i+1);
          pw.print(" ");
          pw.println(j+1);
        }
      }
    }

    br.close();
    pw.close();
  }

  private static class Comp {
    int id;
    List<Comp> nbs = new ArrayList<>();
    List<Integer> values = new ArrayList<>();

    public Comp(int id) {
      this.id = id;
    }

    public void add(int id, int value) {
      nbs.add(companies[id]);
      values.add(value);
    }

    @Override
    public String toString() {
      return Integer.toString(id);
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