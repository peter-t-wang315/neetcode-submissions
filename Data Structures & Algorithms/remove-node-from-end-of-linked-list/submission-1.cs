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
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        if (head.next == null) {
            return null;
        }

        ListNode prev = head;
        ListNode fast = prev.next;

        for (int i = 1; i < n; i++) {
            if (fast.next == null) {
                return head.next;
            }
            fast = fast.next;
        }

        while (fast.next != null) {
            prev = prev.next;
            fast = fast.next;
        }

        prev.next = prev.next.next;

        return head;
    }
}
