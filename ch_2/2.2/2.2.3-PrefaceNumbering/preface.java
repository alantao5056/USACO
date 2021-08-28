/*
ID: alantao
LANG: JAVA
TASK: preface
*/

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.nio.file.Files;
import java.nio.file.Paths;

public class preface {
  static int N;
  static StringTokenizer st;

  static class RomanNumeral {
    int I, V, X, L, C, D, M;

    RomanNumeral(int I, int V, int X, int L, int C, int D, int M) {
      this.I = I;
      this.V = V;
      this.X = X;
      this.L = L;
      this.C = C;
      this.D = D;
      this.M = M;
    }

    public void add(RomanNumeral r) {
      this.I += r.I;
      this.V += r.V;
      this.X += r.X;
      this.L += r.L;
      this.C += r.C;
      this.D += r.D;
      this.M += r.M;
    }
  }

  static RomanNumeral[] onesPlace = {new RomanNumeral(1, 0, 0, 0, 0, 0, 0), new RomanNumeral(2, 0, 0, 0, 0, 0, 0), new RomanNumeral(3, 0, 0, 0, 0, 0, 0), new RomanNumeral(1, 1, 0, 0, 0, 0, 0), new RomanNumeral(0, 1, 0, 0, 0, 0, 0), new RomanNumeral(1, 1, 0, 0, 0, 0, 0), new RomanNumeral(2, 1, 0, 0, 0, 0, 0), new RomanNumeral(3, 1, 0, 0, 0, 0, 0), new RomanNumeral(1, 0, 1, 0, 0, 0, 0)};
  static RomanNumeral[] tensPlace = {new RomanNumeral(0, 0, 1, 0, 0, 0, 0), new RomanNumeral(0, 0, 2, 0, 0, 0, 0), new RomanNumeral(0, 0, 3, 0, 0, 0, 0), new RomanNumeral(0, 0, 1, 1, 0, 0, 0), new RomanNumeral(0, 0, 0, 1, 0, 0, 0), new RomanNumeral(0, 0, 1, 1, 0, 0, 0), new RomanNumeral(0, 0, 2, 1, 0, 0, 0), new RomanNumeral(0, 0, 3, 1, 0, 0, 0), new RomanNumeral(0, 0, 1, 0, 1, 0, 0)};
  static RomanNumeral[] hundredsPlace = {new RomanNumeral(0, 0, 0, 0, 1, 0, 0), new RomanNumeral(0, 0, 0, 0, 2, 0, 0), new RomanNumeral(0, 0, 0, 0, 3, 0, 0), new RomanNumeral(0, 0, 0, 0, 1, 1, 0), new RomanNumeral(0, 0, 0, 0, 0, 1, 0), new RomanNumeral(0, 0, 0, 0, 1, 1, 0), new RomanNumeral(0, 0, 0, 0, 2, 1, 0), new RomanNumeral(0, 0, 0, 0, 3, 1, 0), new RomanNumeral(0, 0, 0, 0, 1, 0, 1)};
  static RomanNumeral[] thousandsPlace = {new RomanNumeral(0, 0, 0, 0, 0, 0, 1), new RomanNumeral(0, 0, 0, 0, 0, 0, 2), new RomanNumeral(0, 0, 0, 0, 0, 0, 3)};

  private static int getInt() {
    return Integer.parseInt(st.nextToken());
  }

  private static RomanNumeral getRomanNumerals() {
    RomanNumeral result = new RomanNumeral(0, 0, 0, 0, 0, 0, 0);
    for (int i = 1; i < N + 1; i++) {
      if (i%10 - 1 != -1) {
        RomanNumeral ones = onesPlace[i%10 - 1];
        result.add(ones);
      }
      if (i > 9 && (i/10)%10 - 1 != -1) {
        RomanNumeral tens = tensPlace[(i/10)%10 - 1];
        result.add(tens);
      }

      if (i > 99 && (i/100)%10 - 1 != -1) {
        RomanNumeral hundreds = hundredsPlace[(i/100)%10 - 1];
        result.add(hundreds);
      }

      if (i > 999 && (i/1000)%10 - 1 != -1) {
        RomanNumeral thousands = thousandsPlace[(i/1000)%10 - 1];
        result.add(thousands);
      }
    }
    return result;
  }

  public static void main(String[] args) throws IOException{
    String in = new String(Files.readAllBytes(Paths.get("preface.in")));
    st = new StringTokenizer(in);
    PrintWriter pw = new PrintWriter(new FileWriter("preface.out"));

    N = getInt();

    RomanNumeral result = getRomanNumerals();
    pw.printf("I %d\n", result.I);
    if (result.V != 0) {
      pw.printf("V %d\n", result.V);
    }
    if (result.X != 0) {
      pw.printf("X %d\n", result.X);
    }
    if (result.L != 0) {
      pw.printf("L %d\n", result.L);
    }
    if (result.C != 0) {
      pw.printf("C %d\n", result.C);
    }
    if (result.D != 0) {
      pw.printf("D %d\n", result.D);
    }
    if (result.M != 0) {
      pw.printf("M %d\n", result.M);
    }

    pw.close();
  }
}