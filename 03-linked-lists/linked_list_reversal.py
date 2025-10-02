"""
Linked List Reversal
Reverse a singly linked list

1 -> 2 -> 4 -> 7 -> 3

3 -> 7 -> 4 -> 2 -> 1

1. Save a referente to the next node (next_node = curr_node.next)
2. Change de current node's next pointer to link to the previous node
(curre_node.next = prev_node)
3. Move both prev_node and curr_node forward by one
(prev_node = curr_node, curr_node = next_node)
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
        nodes.append("None")
        return " -> ".join(nodes)


def linked_list_reversal(head: ListNode) -> ListNode:
    curr_node, prev_node = head, None
    # 1 -> 2 -> 4 -> 7 -> 3
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    return prev_node


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


# Helper function to convert a linked list back to a Python list for easy printing
def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    items = []
    current = head
    while current:
        items.append(current.val)
        current = current.next
    return items


if __name__ == "__main__":
    my_list = [1, 2, 4, 7, 3]

    original_head = create_linked_list(my_list)

    reversed_head = linked_list_reversal(original_head)

    print(reversed_head)
