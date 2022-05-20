import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

class Solution {
  public int value(char r) {
    if (r == 'I')
      return 1;
    if (r == 'V')
      return 5;
    if (r == 'X')
      return 10;
    if (r == 'L')
      return 50;
    if (r == 'C')
      return 100;
    if (r == 'D')
      return 500;
    if (r == 'M')
      return 1000;
    return -1;
  }

  public int romanToInt(String s) {
    // System.out.println(s);
    int sum = 0;
    for (int i = 0; i < s.length(); i++) {
      int v = value(s.charAt(i));
      if (i + 1 < s.length()) {
        int v2 = value(s.charAt(i + 1));
        if (v >= v2) {
          sum += v;
        } else {
          sum -= v;
        }
      } else {
        sum += v;
      }
    }
    return sum;
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    String n = scanner.nextLine();

    var sol = new Solution();
    int a = sol.romanToInt(n);

    System.out.println(a);
  }
}