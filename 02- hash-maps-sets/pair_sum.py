"""
Properties of hash maps:
- Data is stored in the form of key-value pairs.
- Hash maps don't store duplicates
- Hash maps are unordered data structures, meaning keys are not stored in any
specific order.

Time complexity breakdown

Operation   Average case    Worst case  Description
Insert          O(1)            O(n)    add a key-value pair to the hash map.
Access          O(1)            O(n)    find or retrieve an element
Delete          O(1)            O(n)    delete a key-value pair.

When to use hash maps or sets
Hash maps -> dictionaries, couting frequencies, storing key-value pair
    and handling scenarios requiring quick lookups
Hash sets -> store unique elements, marking elements as used or visited,
    and checking for duplicates.
    
Real-world Example
Web Browser cache: Hash maps and sets used everywhere in real-world systems.
A classiec example of hash maps in action is in caching system within web 
browser. When you visit a website, your browser stores data such as images,
HTML, and CSS files in a cache so it can load much faster on future visits.
"""

"""
Pair Sum - Unsorted

Given an array of integers, return indexes of any two numbers that add up
to a target. The order doesn't matter.

Input: nums = [-1, 3, 4, 2], target=3
Output: [0, 2]

nums[0] + nums [2] = -1 + 4 = 3
"""
from typing import List  # noqa: E402


"""
nums = [-1, 3, 4, 2] target = 3

num_map = {
    -1: 0
     3: 1
     4: 2
     2: 3
}

1. (0, -1) -> complement=3-(-1)=4 -> True and 2 != 0
"""


def pair_sum_unsorted_two_pass(nums: List[int], target: int) -> List[int]:
    num_map = {}
    for i, num in enumerate(nums):
        num_map[num] = i

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map and num_map[complement] != i:
            return [i, num_map[complement]]

    return []


"""
nums = [-1, 3, 4, 2] target = 3

1. -1 --> has_map {} --> hashmap doesn't contain -1 complement(4)
    - add (-1, 0)
2. 3 --> has_map {-1: 0} --> doesn't contai 3 complement(0)
    - add (3, 1)
3. 4 --> hashmap {-1:0, 3:1} -->  complement(-1) contains 4
    - [0, 2]
    
Time complexity --> 0(n) because we iterate though each element
in the nums array once and perform constant-time

Space complexity --> O(n) since the hashmap can grow up to n in size. 
"""


def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return []


# if __name__ == '__main__':
#     nums = [-1, 3, 4, 2]
#     target = 3
#     pair_sum_unsorted_two_pass(nums, target)
