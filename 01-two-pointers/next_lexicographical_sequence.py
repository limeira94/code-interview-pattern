"""
Next Lexicographical Sequence

Given a string of lowercase English letters, rearrange the characters to form
a new string representing the next immediate sequence in lexicographical order.
If the given string is already last in lexicographical order among all possible
arrangements, return the arrangement that's first in lexicographical order.

Input s = 'dcba'
Output = 'abcd'

Example:
    [a, b, c, e, d, d, a]
    1. [d, a] --> non-increasing
    2. [d, d, a] --> non-increasing
    3. [e, d, d, a] --> non-increasing
    4. [c, e, d, d, a] --> not non-increasing --> can rearrange to incur an increase
    5. c --> pivot
"""


def next_lexicographical_sequence(s: str) -> str:
    letters = list(s)
    pivot = len(letters) - 2
    while pivot >= 0 and letters[pivot] >= letters[pivot + 1]:
        pivot -= 1

    if pivot == -1:
        return "".join(reversed(letters))

    rightmost_successor = len(letters) - 1
    while letters[rightmost_successor] <= letters[pivot]:
        rightmost_successor -= 1

    letters[pivot], letters[rightmost_successor] = (
        letters[rightmost_successor],
        letters[pivot],
    )

    letters[pivot + 1 :] = reversed(letters[pivot + 1 :])
    return "".join(letters)


if __name__ == "__main__":
    s = "abcedda"
    
    next_lexicographical_sequence(s) # result is "abdacde"
