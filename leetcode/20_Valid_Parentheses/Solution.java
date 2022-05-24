class Solution {
  public boolean isValid(String s) {
    return false;
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    scanner.nextLine();
    var sol = new Solution();
    for (int i = 0; i < n; i++) {
      String s = scanner.nextLine();
      Boolean a = sol.isValid(s);
      System.out.println("Case " + i + ": [ " + s + " ]" + a);
    }
    scanner.close();
  }
}