class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def double_number(head):
    carry = 0
    current = head
    dummy = ListNode(0)  
    dummy.next = head
    prev = dummy

    while current:
        new_val = current.val * 2 + carry
        current.val = new_val % 10
        carry = new_val // 10
        prev = current
        current = current.next

    if carry > 0:
        prev.next = ListNode(carry)

    return dummy.next

def list_print(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


head = ListNode(1, ListNode(2, ListNode(3)))
result = double_number(head)
print(list_print(result)) 
