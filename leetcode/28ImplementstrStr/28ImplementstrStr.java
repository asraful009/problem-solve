class Solution {
  public int strStr(String haystack, String needle) {
    int pos = -1;
    pos = haystack.indexOf(needle);
    return pos;
  }

  public static void main(String[] args) {
    String haystack = "aaaaa";
    String needle = "bba";
    var s = new Solution();
    System.out.println(s.strStr(haystack, needle));
  }
}