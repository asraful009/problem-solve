import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

class Solution {

  public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    ListNode curr = null;
    ListNode head = null;
    List<Integer> arr = new ArrayList<>();
    curr = list1;
    while (curr != null) {
      arr.add(curr.val);
      curr = curr.next;
    }
    curr = list2;
    while (curr != null) {
      arr.add(curr.val);
      curr = curr.next;
    }
    Collections.sort(arr);

    for (int i = 0; i < arr.size(); i++) {
      if (head == null) {
        head = new ListNode();
        curr = head;
        curr.val = arr.get(i);
        curr.next = null;
      } else {
        ListNode temp = new ListNode();
        temp.val = arr.get(i);
        temp.next = null;
        curr.next = temp;
        curr = temp;
      }

    }
    return head;
  }

  public void print(ListNode head) {
    ListNode curr = head;
    while (curr != null) {
      System.out.println(curr + " -> " + curr.val + " ==> " + curr.next);
      curr = curr.next;
    }
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    String[] line1 = scanner.nextLine().split(" ");
    String[] line2 = scanner.nextLine().split(" ");
    ListNode head1 = null;
    ListNode curr = null;
    ListNode head2 = null;
    for (String l : line1) {
      if (l.length() == 0)
        break;
      ListNode node = new ListNode();
      node.val = Integer.parseInt(l);
      node.next = null;
      if (head1 == null) {
        head1 = node;
        curr = head1;
      } else {
        curr.next = node;
        curr = node;
      }
    }
    curr = null;
    for (String l : line2) {
      if (l.length() == 0)
        break;
      ListNode node = new ListNode();
      node.val = Integer.parseInt(l);
      node.next = null;
      if (head2 == null) {
        head2 = node;
        curr = head2;
      } else {
        curr.next = node;
        curr = node;
      }
    }
    curr = head1;
    while (curr != null) {
      System.out.println(curr.val);
      curr = curr.next;
    }
    System.out.println();
    curr = head2;
    while (curr != null) {
      System.out.println(curr.val);
      curr = curr.next;
    }
    // strs.stream().forEach(System.out::println);
    var sol = new Solution();
    System.out.println("+==========================+");
    ListNode a = sol.mergeTwoLists(head1, head2);
    System.out.println("+==========================+");
    curr = a;
    while (curr != null) {
      System.out.println(curr.val);
      curr = curr.next;
    }
    System.out.println("+--------------------------------+");
    // System.out.println("-> " + a);
    scanner.close();
  }
}