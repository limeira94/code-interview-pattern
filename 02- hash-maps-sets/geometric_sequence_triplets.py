"""
Geometric Sequence Triplets

Is a sequence of three numbers where each successive number is obtained by
multiplying the preceding number by a constant called the common ratio.
- 1, 2, 4 is a geometric sequence with a ratio 2 -> 1*2=2 and 2*2=4
- 5, 15, 45 is a geometric sequence with a ratio 3 -> 5*3=15 and 
- 2, 3, 4 not a geometric sequence

Rules:
1. It consists of three values that follow a geometric sequence with a common ratio r
2. The three value forming the triplet must appear in the same order within the array as they do in the geometric sequence. 
This means for a geometric triplet (nums[i], nums[j], nums[k]), the indexes must follow the order i<j<k

(x, x*r, x*r^2)

Input: [2, 1, 2, 4, 8, 8], r=2
Output: 5

{
    2: 2,
    1: 1,
    4: 1,
    8: 2
}
"""
from typing import List
from collections import defaultdict

def geometric_sequence_triplet(nums: List[int], r: int) -> int:
    
    left_map = defaultdict(int)
    right_map = defaultdict(int)
    count = 0
    
    for x in nums:
        right_map[x] += 1
    
    for x in nums:
        right_map[x] -= 1
        
        if x % r == 0:
            count += left_map[x // r] * right_map[x * r]
        
        left_map[x] += 1
    
    return count
