
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

class Solution {
  public boolean isPalindrome(int x) {
    if (x < 0) {
      return false;
    }
    if (x == 0) {
      return true;
    }
    String str = String.format("%d", x);
    String nstr = "";
    char ch;
    for (int i = 0; i < str.length(); i++) {
      ch = str.charAt(i); // extracts each character
      nstr = ch + nstr; // adds each character in front of the existing string
    }
    if (str.equals(nstr)) {
      return true;
    }
    return false;
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    int n = scanner.nextInt();

    var sol = new Solution();
    boolean a = sol.isPalindrome(n);

    System.out.println(a);
  }
}