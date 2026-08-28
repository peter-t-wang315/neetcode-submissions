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

 // [1, 2, 3, 4, 5, 6] l: 2 r: 4
 // [1, 4, 3, 2, 5, 6]
public class Solution {
    public ListNode ReverseBetween(ListNode head, int left, int right) {
        if (head == null || left == right) {
            return head;
        }

        ListNode dummyHead = new(0);
        dummyHead.next = head;

        ListNode prev = dummyHead;
        for (int i = 0; i < left - 1; i++) {
            prev = prev.next;
        }

        ListNode curr = prev.next;
        for (int i = 0; i < right - left; i++) {
            ListNode rNode = curr.next;
            curr.next = rNode.next;
            rNode.next = prev.next;
            prev.next = rNode;
        }

        return dummyHead.next;
    }
}