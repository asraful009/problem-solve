class Solution {
  // you need to treat n as an unsigned value
  public int hammingWeight(int n) {
    long unsignedValue = n & 0xffffffffL;
    int count = 0;
    while (unsignedValue > 0) {
      unsignedValue = unsignedValue & (unsignedValue - 1);
      count++;
    }
    return count;
  }

  public static void main(String[] args) {
    Solution s = new Solution();
    System.out.println(s.hammingWeight(-3));
  }
}