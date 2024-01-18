class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(4)
head.next.next.next = ListNode(-2)
head.next.next.next.next = ListNode(0)
head.next.next.next.next.next = head.next  
print(cycle(head))
