public class Insert {
  public ListNode insert(ListNode head, int x) {
    if (head == null) {
      ListNode newNode = new ListNode(x);
      newNode.next = newNode;
      return newNode;
    }
    ListNode prev = head;
    ListNode curr = head.next;
    boolean toInsert = true;
    do {
      if (prev.val <= x && x <= curr.val) {
        toInsert = true;
      } else if (prev.val > curr.val) {
        if (x >= prev.val || x <= curr.val) {
          toInsert = true;
        }
      }
      if (toInsert) {
        prev.next = new ListNode(x, curr);
        return head;
      }
      prev =  curr ;
      curr = curr.next;

    } while (prev != head);
  
    prev.next = new ListNode(x,curr);
    return head;
  }
}
