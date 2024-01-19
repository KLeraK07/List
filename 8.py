class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    def reverse_list(start, end):
        prev, current = None, start
        while current != end:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

    def get_length(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    length = get_length(head)

    if length < k:
        return head

    group_end = head
    for _ in range(k - 1):
        group_end = group_end.next

    next_group_start = group_end.next

    # Перевертання групи
    reversed_group_start = reverse_list(head, next_group_start)

    # Підключення перевернутої групи до решти списку
    head.next = reverse_k_group(next_group_start, k)

    return reversed_group_start

def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Приклад
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2
result = reverse_k_group(head, k)
print(print_list(result))  # Виведе: [2, 1, 4, 3, 5]
