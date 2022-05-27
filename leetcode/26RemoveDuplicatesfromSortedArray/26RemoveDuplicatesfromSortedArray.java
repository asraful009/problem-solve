import java.util.Iterator;
import java.util.Scanner;
import java.util.SortedSet;
import java.util.TreeSet;

class Solution {
  public int removeDuplicates(int[] nums) {
    int k = 0, i = 0;
    SortedSet<Integer> set = new TreeSet<>();
    for (i = 0; i < nums.length; i++) {
      set.add(nums[i]);
    }
    k = set.size();
    Iterator<Integer> it = set.iterator();
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
    int k = sol.removeDuplicates(nums);
    System.out.println("+================================+");
    sol.print(nums);
    System.out.println("+================================+");
    System.out.println(k);
    System.out.println("+--------------------------------+");
    scanner.close();
  }
}