import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Solution {
    public String longestCommonPrefix(String[] strs) {

        if (strs.length == 0) {
            return "";
        }
        if (strs.length == 1) {
            return strs[0];
        }

        String match = strs[0];

        for (int i = 1; i < strs.length; i++) {
            String currStr = strs[i];
            // System.out.println(currStr + " -> " + match);
            if (currStr.length() < match.length()) {
                match = match.substring(0, currStr.length());
            }
            // System.out.println(match);
            for (int j = 0; j < match.length(); j++) {
                if (match.charAt(j) == currStr.charAt(j)) {
                    continue;
                } else {
                    match = match.substring(0, j);
                    break;
                }
            }
        }
        return match;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        // System.out.println(n);
        scanner.nextLine();
        List<String> strs = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            strs.add(scanner.nextLine());
        }
        // strs.stream().forEach(System.out::println);
        var sol = new Solution();
        String a = sol.longestCommonPrefix(strs.stream().toArray(String[]::new));

        System.out.println("-> " + a);
        scanner.close();
    }
}