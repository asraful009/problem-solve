import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

class Solution {
  public int removeElement(int[] nums, int val) {

    int k = 0, i = 0;
    List<Integer> arr = new LinkedList<>();
    for (i = 0; i < nums.length; i++) {
      if (nums[i] == val) {
        continue;
      }
      arr.add(nums[i]);
    }
    k = arr.size();
    Iterator<Integer> it = arr.iterator();
    i = 0;
    while (it.hasNext()) {
      int v = it.next();
      // System.out.println(v);
      nums[i++] = v;
    }
    return k;
  }

  public void print(int[] nums) {
    for (int i = 0; i < nums.length; i++) {
      System.out.print(nums[i] + " ");
    }
    System.out.println();
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    String[] numbersStr = scanner.nextLine().split(" ");
    String vStr = scanner.nextLine();
    int val = Integer.parseInt(vStr);
    int[] nums = new int[numbersStr.length];
    int i = 0;
    for (String l : numbersStr) {
      if (l.length() == 0)
        break;
      nums[i] = Integer.parseInt(l);
      i++;
    }
    var sol = new Solution();
    sol.print(nums);
    System.out.println("+--------------------------------+");
    int k = sol.removeElement(nums, val);
    System.out.println("+================================+");
    sol.print(nums);
    System.out.println("+================================+");
    System.out.println(k);
    System.out.println("+--------------------------------+");
    scanner.close();
  }
}