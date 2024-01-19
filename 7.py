import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def k_lists(lists):
    heap = []
    for lst in lists:
        while lst:
            heapq.heappush(heap, lst.val)
            lst = lst.next

    dummy = ListNode()
    current = dummy

    while heap:
        current.next = ListNode(heapq.heappop(heap))
        current = current.next

    return dummy.next

def list_print(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Приклад
lists = [
    ListNode(-1, ListNode(2, ListNode(5))),
    ListNode(0, ListNode(2, ListNode(3, ListNode(4)))),
    ListNode(1, ListNode(6))
]

result = k_lists(lists)
print(list_print(result)) 
