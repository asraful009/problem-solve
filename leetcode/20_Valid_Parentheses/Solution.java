import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

class Solution {
  public char revParnt(char c) {
    if (c == '(')
      return ')';
    if (c == '{')
      return '}';
    if (c == '[')
      return ']';
    return ' ';
  }

  public boolean isValid(String s) {
    if (s.length() % 2 == 1) {
      return false;
    }
    List<Character> stack = new LinkedList<>();
    stack.add(s.charAt(0));
    for (int i = 1; i < s.length(); i++) {
      char c = s.charAt(i);
      if (c == '(' || c == '{' || c == '[') {
        stack.add(c);
      } else {
        if (stack.size() == 0) {
          return false;
        }
        // System.out.println(stack.get(stack.size() - 1) + "==" + c);
        if (revParnt(stack.get(stack.size() - 1)) == c) {
          stack.remove(stack.size() - 1);
        } else {
          return false;
        }
        // System.out.println(c + " -> " + stack.get(i - 1));
      }
      // System.out.println(c + " -> " + stack.get(stack.size() - 1));
    }
    return stack.size() == 0 ? true : false;
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    scanner.nextLine();
    var sol = new Solution();
    for (int i = 0; i < n; i++) {
      String s = scanner.nextLine();
      Boolean a = sol.isValid(s);
      System.out.println("Case " + i + ": [ '" + s + "' ] => " + a);
    }
    scanner.close();
  }
}