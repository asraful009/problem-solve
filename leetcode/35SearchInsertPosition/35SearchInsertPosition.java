class Solution {
  public int searchInsert(int[] nums, int target) {

    int s = 0;
    int e = nums.length - 1;
    int ret = -1;
    int mid = 0;
    while (s <= e) {
      mid = s + (e - s) / 2;
      if (nums[mid] == target) {
        return mid;
      }

      if (nums[mid] > target) {
        e = mid - 1;
      } else {
        ret = mid;
        s = mid + 1;
      }
    }
    return ret + 1;
  }

  public static void main(String[] args) {
    int[] nums = new int[] { 1, 3, 5, 6 };
    int target = 5;
    var s = new Solution();
    System.out.println(s.searchInsert(nums, target));
  }
}