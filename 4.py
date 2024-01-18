class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head):
    def reverse_list(node):
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev

    def merge_lists(list1, list2):
        while list2:
            temp1, temp2 = list1.next, list2.next
            list1.next, list2.next = list2, temp1
            list1, list2 = temp1, temp2

    if not head or not head.next:
        return head

    # Знаходимо середину списку
    slow, fast = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    reversed_second_half = reverse_list(slow.next) # Реверсуємо другу половину списку
    slow.next = None
    merge_lists(head, reversed_second_half) # Об'єднуємо дві половини списку
    return head

def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

head = ListNode(-1, ListNode(2, ListNode(0, ListNode(5, ListNode(3, ListNode(1))))))
result = reorder_list(head)
print(print_list(result))  
