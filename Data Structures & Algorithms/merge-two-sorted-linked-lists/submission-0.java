/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head = null;
        ListNode base_pointer = null;

        while (true) {


            boolean l1_pointer_null = list1 == null;
            boolean l2_pointer_null = list2 == null;
            ListNode chosen;

            // Select from which list to choose
            if (l1_pointer_null && l2_pointer_null) {
                chosen = null;
            } else if (l1_pointer_null) {
                chosen = list2;
                list2 = list2.next;
            } else if (l2_pointer_null) {
                chosen = list1;
                list1 = list1.next;
            } else if (list1.val > list2.val) {
                chosen = list2;
                list2 = list2.next;
            } else {
                chosen = list1;
                list1 = list1.next;
            }

            // Check to stop
            if (chosen == null) {
                break;
            }

            // Append
            if (head == null) {
                head = chosen;
                base_pointer = head;
            } else {
                head.next = chosen;
                head = head.next;
            }
        }

        return base_pointer;
    }
}