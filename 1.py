class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def new_list(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val <= list2.val:
        list1.next = new_list(list1.next, list2)
        return list1
    else:
        list2.next = new_list(list1, list2.next)
        return list2

def list_print(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

list1 = ListNode(-1, ListNode(0, ListNode(2, ListNode(5))))
list2 = ListNode(1, ListNode(2, ListNode(4, ListNode(7))))
result = new_list(list1, list2)
print(list_print(result))  
