"""
Remove the Kth Last Node From a Linked List

We need to find the node directly before the kth last node
a -> b -> c

a -> c
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        nodes = []
        curr = self
        while curr:
            nodes.append(str(curr.val))
            curr = curr.next
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


def remove_kth_last_node(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(-1)
    dummy.next = head
    trailer = leader = dummy

    for _ in range(k):
        leader = leader.next
        if not leader:
            return head

    while leader.next:
        leader = leader.next
        trailer = trailer.next

    trailer.next = trailer.next.next
    return dummy.next


if __name__ == "__main__":
    my_list = [1, 2, 4, 7, 3]
    create_list = create_linked_list(my_list)

    remove_last = remove_kth_last_node(create_list, 2)

    print(remove_last)
