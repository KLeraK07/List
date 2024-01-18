class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete(head):
    if not head or not head.next:
        return head

    if head.val == head.next.val:
        head.next = head.next.next
        delete(head)
    else:
        delete(head.next)

    return head

def list_print(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4)))))))
result = delete(head)
print("Результат:",list_print(result))  
