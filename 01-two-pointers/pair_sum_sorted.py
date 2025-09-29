"""
Pair Sum - Sorte
Example 1
Input: nums = [-5, -2, 3, 4, 6], target = 7
Output: [2, 3]
Explanation --> nums[2] + nums[3] = 3 + 4 = 7

Example 2
Input: nums = [1, 1, 1], target = 2
Output: [0, 1]
Explanation --> other valid outputs coulb be 
    [1, 0], [0, 2], [ 2, 0], [2, 1]

The brute force solution to this problem involves checking all possibles pairs.
"""
from typing import List

def pai_sum_sorted_brute_force(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n): # [0, 1, 2, 3, 4]
        for j in (i + 1, n): # [1, 2, 3, 4]
            if nums[i] + nums[j] == target:
                return [i, j]
    return [] 

"""
nums = [-5, -2, 3, 4, 6]
1. [0, 1, 2, 3, 4]
2. [1, 2, 3, 4]
Compartion:
First --> [0, 1] --> -5 - 2 == 7 --> False
Second --> [1, 2] --> -2 + 3 == 7 --> False
Third --> [2, 3] --> 3 + 4 == 7 --> True
Return --> [2, 3] 
"""

"""
This approach has a time complexity of O(n^2), where n denotes
length of the array. This approach does not take into account that
the input array is sorted.
Could we use this fact to come up with a more efficient solution?

A good place to start it by looking at the smallest and largest values:
the first and last elements, respectively.
"""

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        pair_sum = nums[left] + nums[right]
        if pair_sum < target:
            left += 1
        elif pair_sum > target:
            right -= 1
        else:
            return [left, right]
    return []
    
"""
Time complexity: pair_sum_sorted is O(n) because we perform approximately n
interarions using two-pointers technique in the worst case.
Space complexity: We only allocated a constant number of variables, so the
space complexity is O(1)
"""

"""
Interview Tip
When interviewers pose a problem, they sometimes provide only the minimum
amount of information required for you start solving it. Consequently, it's
crucial to thoroughly evaluate all that information to determine which
details are essential for solving the problem efficiently. In this problem,
the key to arriving at the optimal soluiton is recognizing that the input
is sorted.
"""