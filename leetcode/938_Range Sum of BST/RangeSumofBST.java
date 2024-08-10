import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.Array;
import java.util.Arrays;

class RangeSumofBST {
  public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
      this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
      this.val = val;
      this.left = left;
      this.right = right;
    }

    @Override
    public String toString() {
      return "{ " +
          "\"val\":" + val +
          ", \"left\" :" + left +
          ", \"right\" :" + right +
          " }";
    }
  }

  public TreeNode generaTreeNode(Integer[] arr) {
    if (arr == null || arr.length == 0) {
      return null;
    }
    return generaTreeNode(arr, 0);
  }

  private TreeNode generaTreeNode(Integer[] arr, int index) {
    if (arr == null || arr.length == 0) {
      return null;
    }

    if (index >= arr.length || arr[index] == null) {
      return null;
    }

    TreeNode node = new TreeNode(arr[index]);
    node.left = generaTreeNode(arr, index * 2 + 1);
    node.right = generaTreeNode(arr, index * 2 + 2);
    return node;
  }

  public int rangeSumBST(TreeNode root, int low, int high) {
    // System.out.println("**********");
    // System.out.println(root);
    if (root == null) {
      return 0;
    }
    if ((root.left == null && root.right == null) && (root.val == low || root.val == high)) {
      return root.val;
    }

    int leftV = 0, rightV = 0, val = 0;
    leftV = rangeSumBST(root.left, low, high);
    rightV = rangeSumBST(root.right, low, high);
    val = (root.val >= low && root.val <= high) ? root.val : 0;
    // System.out.println(val + " + " + leftV + " + " + rightV);
    return val + leftV + rightV;
  }

  public static void main(String[] args) {
    String filePath = "i.txt";

    try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
      String line;
      while ((line = br.readLine()) != null) {
        String trimmedInput = line.substring(1, line.length() - 1);
        Integer[] arr = Arrays.stream(trimmedInput.split(","))
            .map(v -> v.equals("null") ? null : Integer.parseInt(v))
            .toArray(Integer[]::new);
        System.out.println(Arrays.toString(arr));
        int low = 0, high = 0;
        line = br.readLine();
        if (line != null) {
          low = Integer.parseInt(line);
        }
        line = br.readLine();
        if (line != null) {
          high = Integer.parseInt(line);
        }
        RangeSumofBST rangeSumofBST = new RangeSumofBST();
        TreeNode root = rangeSumofBST.generaTreeNode(arr);
        // System.out.println(low + " " + high);
        // System.out.println(root);
        // System.out.println("---------------------------");
        System.out.println(rangeSumofBST.rangeSumBST(root, low, high));
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
