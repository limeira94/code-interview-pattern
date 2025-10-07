"""
Linked List Intersection

"""

from typing import Optional, List


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        nodes = []
        curr = self
        while curr:
            nodes.append(str(curr.val))
            curr = curr.next
        nodes.append("None")
        return " -> ".join(nodes)


# Helper function to create a linked list from a Python list
def create_linked_list(items: List[int]) -> Optional[ListNode]:
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head


"""
A: [1, 3, 4, 8, 7, 2]
B: [6, 4, 8, 7, 2]

prt_A = [1, 3, 4, 8, 7, 2], prt_B = [6, 4, 8, 7, 2]

1. prt_A =  3, 4, 8, 7, 2, prt_B = 4, 8, 7, 2
2. prt_A = 4, 8, 7, 2, prt_B = 8, 7, 2
3. prt_A = 8, 7, 2, prt_B = 7, 2
4. prt_A = 7, 2, prt_B = 2
5. prt_A = 2, prt_B = 1, 3, 4, 8, 7, 2
6. prt_A = 6, 4, 8, 7, 2, prt_B = 3, 4, 8, 7, 2
7. prt_A = 4, 8, 7, 2, prt_B = 4, 8, 7, 2
8. prt_A == prt_B = 4, 8, 7, 2
"""


def linked_list_intersection(head_A: ListNode, head_B: ListNode) -> ListNode:
    prt_A, prt_B = head_A, head_B

    while prt_A != prt_B:
        prt_A = prt_A.next if prt_A else head_B
        prt_B = prt_B.next if prt_B else head_A

    return prt_A


if __name__ == "__main__":
    list_A = [1, 3, 4, 8, 7, 2]
    list_B = [6, 4, 8, 7, 2]

    create_linked_list_a = create_linked_list(list_A)
    create_linked_list_b = create_linked_list(list_B)

    list_intersection = linked_list_intersection(
        create_linked_list_a, create_linked_list_b
    )

    print(list_intersection)
