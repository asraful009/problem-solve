
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

class Solution {
  public int[] twoSum1(int[] nums, int target) {
    Map<Integer, Integer> smallArr = new TreeMap<>();
    Map<Integer, Integer> largeArr = new TreeMap<>();

    int mid = (int) Math.ceil(target / 2);
    System.out.println(mid);
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] <= mid) {
        if (smallArr.containsKey(nums[i])) {
          if (largeArr.containsKey(nums[i])) {
            continue;
          }
          largeArr.put(nums[i], i);
          continue;
        }
        smallArr.put(nums[i], i);
      } else {
        // if (nums[i] > target) {
        // continue;
        // }
        if (largeArr.containsKey(nums[i])) {
          continue;
        }

        largeArr.put(nums[i], i);
      }
    }
    arrShow(smallArr);
    arrShow(largeArr);
    for (Map.Entry<Integer, Integer> small : smallArr.entrySet()) {
      int sk = small.getKey(), sv = small.getValue();
      // System.out.println(("[" + sk + ":" + sv + "] "));
      for (Map.Entry<Integer, Integer> large : largeArr.entrySet()) {
        int lk = large.getKey(), lv = large.getValue();
        // System.out.println(("\t[" + lk + ":" + lv + "] "));
        if (sk + lk == target) {
          // System.out.println("ok => " + sv + " , " + lv);
          return new int[] { sv, lv };
        }
        // else if (sk + lk > target) {
        // continue;
        // }

      }
    }
    return new int[] {};
  }

  public int[] twoSum(int[] nums, int target) {
    for (int i = 0; i < nums.length; i++) {
      for (int j = i + 1; j < nums.length; j++) {
        if (nums[i] + nums[j] == target) {
          System.out.println("ok => " + i + " , " + j);
          return new int[] { i, j };
        }
      }
    }
    return new int[] {};
  }

  public void arrShow(Map<Integer, Integer> arr) {
    arr.forEach((k, v) -> System.out.print(("[" + k + ":" + v + "] ")));
    System.out.println();
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    int n = scanner.nextInt();
    int target = scanner.nextInt();
    List<Integer> nums = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      nums.add(scanner.nextInt());
    }
    var sol = new Solution();
    int[] a = sol.twoSum(nums.stream().mapToInt(Integer::intValue).toArray(), target);
    for (int i = 0; i < a.length; i++) {
      System.out.print(a[i] + " ");
    }
    System.out.println();
  }
}