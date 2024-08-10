public class FindKOr {
  public int findKOr(int[] nums, int k) {
    int s = 0;
    int n = 0;
    for (int pos = 0; pos < 32; pos++) {
      System.out.println("pos => " + pos);
      n = 0;
      for (int i = 0; i < nums.length; i++) {
        n += (nums[i] >> pos) & (1);
        System.out.println(((nums[i] >> pos) & (1)) + " " + n);
      }
      if (n >= k)
        s |= (1 << pos);
      System.out.println("s => " + s);
    }
    return s;
  }

  public static void main(String[] args) {
    int[] nums = new int[] { 14, 7, 12, 9, 8, 9, 1, 15 };
    int k = 4;
    var s = new FindKOr();
    System.out.println(s.findKOr(nums, k));
  }
}