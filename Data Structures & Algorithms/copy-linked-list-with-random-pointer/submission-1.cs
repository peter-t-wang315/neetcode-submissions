/*
// Definition for a Node.
public class Node {
    public int val;
    public Node next;
    public Node random;
    
    public Node(int _val) {
        val = _val;
        next = null;
        random = null;
    }
}
*/

public class Solution {
    public Node copyRandomList(Node head) {
        if (head == null){
            return null;
        }
        // First we iterate through and create our result nodes right in place with the current linked list so that we can use it for the random pointers
        Node curr = head;
        Node copy = new (curr.val);
        while (curr != null) {
            copy = new (curr.val);
            copy.next = curr.next;
            curr.next = copy;
            curr = copy.next;
        }

        // Now that we have our result nodes in place with their originals, we can go through again and immediately wire the random pointers right next to each other. Can't also separate the copied nodes from the original because it might break a random pointer that is one we've already passed
        curr = head;
        while (curr != null) {
            curr.next.random = curr.random != null ? curr.random.next : null;
            curr = curr.next.next;
        }

        // Now we just reset both linked lists to the originals as if nothing happened
        Node old = head;
        Node newHead = head.next;
        copy = newHead;
        while (old != null)
        {
            old.next = old.next.next;

            copy.next = copy.next != null ? copy.next.next : null;

            old = old.next;
            copy = copy.next;
        }

        return newHead;
    }
}
