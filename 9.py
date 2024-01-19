class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    dummy_small = ListNode()
    dummy_large = ListNode()
    small, large = dummy_small, dummy_large
    current = head
    
    while current:
        if current.val < x:
            small.next = current
            small = small.next
        else:
            large.next = current
            large = large.next

        current = current.next

    small.next = dummy_large.next
    large.next = None
    return dummy_small.next

def list_print(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

head = ListNode(1, ListNode(3, ListNode(0, ListNode(2, ListNode(4, ListNode(3)))))) 
x = 2
result = partition(head, x)
print(list_print(result))  
