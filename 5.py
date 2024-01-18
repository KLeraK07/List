class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete(node):
    if not node or not node.next:
        return
    
    next_node = node.next
    node.val = next_node.val
    node.next = next_node.next

def list_print(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


head = ListNode(-1, ListNode(0, ListNode(2, ListNode(-3, ListNode(5, ListNode(1))))))
node = head.next.next 
delete(node)
print(list_print(head))  
