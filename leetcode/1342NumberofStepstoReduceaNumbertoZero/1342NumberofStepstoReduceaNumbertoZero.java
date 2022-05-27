class Solution {
  public int numberOfSteps(int num) {
    int count = 0;
    while (num > 0) {
      num = (num & 1) == 1 ? (num - 1) : (num >> 1); // num & 1 ==> num%2
      count++;
    }
    return count;
  }

  public static void main(String[] args) {
    Solution s = new Solution();
    System.out.println(s.numberOfSteps(14));
  }
}