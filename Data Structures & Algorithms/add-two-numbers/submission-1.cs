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
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode head = new();
        ListNode curr = head;

        while (l1 != null || l2 != null || carry == 1) {
            int num1 = l1 == null ? 0 : l1.val;
            int num2 = l2 == null ? 0 : l2.val;

            int sum = num1 + num2 + carry;
            if (sum >= 10) {
                carry = 1;
                sum -= 10;
            }
            else {
                carry = 0;
            }

            curr.val = sum;
            if ((l1 != null && l1.next != null) || (l2 != null && l2.next != null) || carry == 1){
                curr.next = new();
            }

            if (l1 != null) {
                l1 = l1.next;
            }
            if (l2 != null) {
                l2 = l2.next;
            }
            if (curr.next != null) {
                curr = curr.next;
            }
        }

        return head;
    }
}
