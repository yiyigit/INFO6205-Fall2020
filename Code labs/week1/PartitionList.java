public class PartitionList {
  public ListNode partition(ListNode head, int x) {
    ListNode l1 = new ListNode(-1);
    ListNode small = l1;
    ListNode l2 = new ListNode(-1);
    ListNode big = l2;
    while (head != null) {
      if (head.val < x) {
        l1.next = head;
        l1 = l1.next;
      } else {
        l2.next = head;
        l2 = l2.next;
      }
    }
    l2.next = null;
    l1.next = big.next;
    return small.next;
  }
}
