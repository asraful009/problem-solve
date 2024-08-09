
public class LargestLocalValuesInAMatrix {

    public int[][] largestLocal(int[][] grid) {
        int[][] ret = new int[grid.length-2][grid[0].length-2];
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                System.out.print(grid[i][j] + " ");
            }
            System.out.print("\n");
        }
        return ret;
    }

    public static void main(String[] args) {
        int[][] matrix = {
            { 9, 9, 8, 1 },
            { 5, 6, 2, 6 },
            { 8, 2, 6, 4 },
            { 6, 2, 2, 2 }
        };
        
        int[][] out = new LargestLocalValuesInAMatrix().largestLocal(matrix);
        for (int i = 0; i < out.length; i++) {
            for (int j = 0; j < out[i].length; j++) {
                System.out.print(out[i][j] + " ");
            }
            System.out.print("\n");
        }
    }
}