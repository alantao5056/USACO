/*
ID: alantao
LANG: JAVA
TASK: frac1
*/

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;
import java.nio.file.Files;
import java.nio.file.Paths;

public class frac1{
  static int N;

  static class Fraction {
    private int top;
    private int bottom;
    Fraction(int top, int bottom) {
      this.top = top;
      this.bottom = bottom;
    }

    @Override
    public String toString() {
      return String.format("%d/%d", top, bottom);
    }

    public int getBottom() {
      return bottom;
    }

    public int getTop() {
      return top;
    }

    public void simplify() {
      int gcf = GCF(top, bottom);
      top /= gcf;
      bottom /= gcf;
    }

    private int GCF(int a, int b) {
      return b==0 ? a : GCF(b, a%b);
    }
  }

  public static void main(String[] args) throws IOException {
    String in = new String(Files.readAllBytes(Paths.get("frac1.in")));
    StringTokenizer st = new StringTokenizer(in);
    PrintWriter pw = new PrintWriter(new FileWriter("frac1.out"));

    N = Integer.parseInt(st.nextToken());

    // get all possible fractions
    List<Fraction> myFractions = new ArrayList<>();
    Set<String> myFractionsSet = new HashSet<>();
    myFractions.add(new Fraction(0, 1));

    for (int i = 1; i < N + 1; i++) {
      // i is for bottom
      for (int j = 1; j < i; j++) {
        // j is for top
        Fraction f = new Fraction(j, i);
        f.simplify();
        if (!myFractionsSet.contains(f.toString())) {
          myFractions.add(f);
          myFractionsSet.add(f.toString());
        }
      }
    }
    myFractions.add(new Fraction(1, 1));
    
    // sorting
    Collections.sort(myFractions, new Comparator<Fraction>() {
      @Override
      public int compare(Fraction o1, Fraction o2) {
        return o1.getTop() * o2.getBottom() - o2.getTop() * o1.getBottom();
      }
    });

    for (Fraction f : myFractions) {
      pw.println(f.toString());
    }

    pw.close();
  }
  
}
