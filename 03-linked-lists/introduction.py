"""
Introduction to Linked Lists

A linked list a data structure consisting of a sequence of nodes, where
each node is a linked to the next.
A node in a linked list has two main components: the data it stores(val) and
a referente to the next node (next) in the sequence
"""
class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next
    
"""
Singly linked list 
Singly linked list can be used to store a collection of data. One of their 
main benefits lies in their dynamic sizing capability, since they can or 
shrink in size flexibly, unlike arrays which are fixed in size.
- frequent insertions and deletions.

Doubly linked list
A doubly linked list is an extend version of the linked list where each
node contains two references: one to the next node (next), and one to the
previous node (prev).
- big advantage is allows for bidirectional traversal

Pointer Manipulation
A useful tip is to visualize pointers as arrows that point from one node
to another, and observe how these arrows should be moved to reflect the 
structural change.

Real-world Example
Music Playlist: Music player applications often use linked lists to implement
playlists, particularly doubly linked lists, where each song node links to
the next and previous songs.
This structure enables efficient addition, removal, and reordering of songs
because only the pointers between nodes need to be updated, rather than moving
the song data in memory.
"""

