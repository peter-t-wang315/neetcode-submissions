/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

public class Solution {
    public void ReorderList(ListNode head) {
        if (head == null || head.next == null) return;
        // Find the halfway point.
        ListNode half = head;
        ListNode fast = head;
        while (fast.next != null && fast.next.next != null) {
            half = half.next;
            fast = fast.next.next;
        }

        // Reverse the second half.
        ListNode prev = null;
        ListNode next = null;
        ListNode current = half.next;
        half.next = null;
        while (current != null) {
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }

        // Merge the pieces now.
        while (prev != null) {
            ListNode tmp1 = head.next;
            ListNode tmp2 = prev.next;

            head.next = prev;
            prev.next = tmp1;

            head = tmp1;
            prev = tmp2;
        }
    }
}
