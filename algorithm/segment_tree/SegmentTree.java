
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.stream.Collectors;

class SegmentTree<X> {

  /**
   * SegmentTreeGenerateLogicFn
   */
  @FunctionalInterface
  public interface SegmentTreeGenerateLogicFn<X> {
    public X compute(X a, X b);
  }

  @FunctionalInterface
  public interface SegmentTreeOutOfBoundaryValueLogicFn<X> {
    public X getOutOfBoundaryValue();
  }

  private int len;
  public X[] segmentTree;
  public SegmentTreeGenerateLogicFn<X> computeLogic;
  public SegmentTreeOutOfBoundaryValueLogicFn<X> boundaryValueLogic;

  @SuppressWarnings("unchecked")
  public SegmentTree(X[] arr,
      SegmentTreeGenerateLogicFn<X> computeLogic,
      SegmentTreeOutOfBoundaryValueLogicFn<X> boundaryValueLogic) {
    len = arr.length;
    segmentTree = (X[]) new Object[arr.length * 4];
    this.computeLogic = computeLogic;
    this.boundaryValueLogic = boundaryValueLogic;
    generateSegmentTree(arr, 0, arr.length - 1, 0);
  }

  private void generateSegmentTree(X[] arr, int start, int end, int index) {
    if (start == end) {
      segmentTree[index] = arr[start];
    } else {
      int mid = (start + end) / 2;
      generateSegmentTree(arr, start, mid, index * 2 + 1);
      generateSegmentTree(arr, mid + 1, end, index * 2 + 2);
      segmentTree[index] = computeLogic.compute(
          segmentTree[index * 2 + 1], segmentTree[index * 2 + 2]);
      // System.out.println(segmentTree[index]);
    }
  }

  private X query(int l, int r, int node, int start, int end) {
    // System.out.println("l:" + l + " r:" + r + " node:" + node + " start:" + start
    // + " end:" + end);
    if (r < start || l > end) {
      return boundaryValueLogic.getOutOfBoundaryValue();
    }
    if (l <= start && r >= end) {
      return segmentTree[node];
    }
    int mid = start + (end - start) / 2;
    X leftX = query(l, r, 2 * node + 1, start, mid);
    X rightX = query(l, r, 2 * node + 2, mid + 1, end);
    return computeLogic.compute(leftX, rightX);
  }

  public void printSegmentTree() {
    if (segmentTree == null) {
      System.out.println("Segment tree is null.");
      return;
    }
    System.out.println(Arrays.toString(segmentTree));
  }

  public X query(int l, int r) {
    return query(l, r, 0, 0, len - 1);
  }

  public static void main(String[] args) {
    String filePath = "i.txt";
    try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
      String line;
      while ((line = br.readLine()) != null) {
        int n = Integer.parseInt(line);
        for (int i = 0; i < n; i++) {
          line = br.readLine();
          if (line != null) {
            int it = Integer.parseInt(line);
            line = br.readLine();
            if (line != null) {
              Integer[] arr = Arrays.stream(line.split(" "))
                  .map(Integer::valueOf).toArray(Integer[]::new);
              System.out.println(Arrays.toString(arr));
              SegmentTreeGenerateLogicFn<Integer> computeLogic = (a, b) -> {
                if (a == null && b == null) {
                  return null;
                } else if (a == null) {
                  return b;
                } else if (b == null) {
                  return a;
                }
                return a >= b ? a : b;
              };
              SegmentTreeOutOfBoundaryValueLogicFn<Integer> boundaryValueLogic = () -> null;
              SegmentTree<Integer> segmentTree = new SegmentTree<Integer>(arr, computeLogic, boundaryValueLogic);
              segmentTree.printSegmentTree();
              line = br.readLine();
              if (line != null) {
                int q = Integer.parseInt(line);
                for (int j = 0; j < q; j++) {
                  line = br.readLine();
                  if (line != null) {
                    Integer[] arrRange = Arrays.stream(line.split(" "))
                        .map(Integer::valueOf).toArray(Integer[]::new);
                    System.out.println(Arrays.toString(arrRange));
                    System.out.println(segmentTree.query(arrRange[0], arrRange[1]));
                  }
                }
              }
            }
          }
        }
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}