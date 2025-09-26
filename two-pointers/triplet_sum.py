"""
Triplet Sum
Given an array of integers, return all triplets [a,b,c] such that
a + b + c = 0. 

The solution not contain duplicate triplets. 
If no such triplets are found, return an empty array.

Each triplet can be arranged in any order, and the output can be returned
in any order.
Example:
Inputs: nums = [0, -1, 2, -3, 1]
Output: [[-3, 1, 2], [-1, 0, 1]]

This solution is quite inefficient whit a time complexity O(n^3)
"""
from typing import List

def triplet_sum_brute_force(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    triplets = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))    
                    triplets.add(triplet)
    return [list(triplet) for triplet in triplets]

"""
For any triplet [a, b, c], we can focus on finding a pair [b, c] that
sums to '-a' (a + b + c = 0 --> b + c = -a)

The first thing is sort the input, for using Pair Sum
[-1 2 -2 1 -1 2] --sort--> [-2 -1 -1 1 2 2]

i=0
Take a pointer "i" and compare pair_sum_sorted([-1 -1 1 2 2], target=2)
Why target = 2? Because is firs pointer in list

When use Pair Sum and left == right --> break
This indicates that there are no triplets starting with -2 that add up to 0
--> pair found: [[1, 1]]
--> triplets formed: [[-2 , 1, 1]]

i=1, num[i] =-1
So, let's increment our main pointer, i, and try again
Now pair_sum_sorted([-1 1 2 2 ], target=1)
sum = 1 == 1 --> pair found [-1 2] --> left += 1
sum = 3 > 1 --> right--
sum = 3 > 1 --> right--
sum = 2 > 1 --> right--
left > right (1 > 0) --> loop terminates
--> pair found [[-1, 2]]
--> triplet formad [[-1, -1, 2]]

[-2 -1 -1 1 2 2]
i=2, num[i] = -1
i > 0 && nums[i] == nums[i - 1]
nums[2] == nums[1] == -1

i=3, num[i] = 1
pair_sum_sorted([2, 2], target=-1)
sum = 4 > -1 right--
sum = 4 > -1 right--
left = 0 right = -1
left > right
--> pair not found []
--> triplet formad []

i=4, num[i]=2
pair_sum_sorted([2], target=-2)
left=0 right=-1
left > right 
--> pair not founr []
-->triplet format []

Result:
[[-2, 1, 1], [-1, -1, 2]]
"""

def triplet_sum(nums: List[int]) -> List[List[int]]:
    triplets = []
    nums.sorts()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        pairs = pair_sum_sorted_all(nums, i + 1, -nums[i])
        for pair in pairs:
            triplets.append([nums[i]] + pair)
    return triplets 

"""
nums = [1, 2, 2, 3, 4, 5, 6, 7] target = 4
pair_num_sorted --> return [0, 3] and stop but I need continue
the return is [[0, 3], [1, 2]]
"""
def pair_sum_sorted_all(nums: List[int], start: int, target: int) -> List[int]:
    left, right = start, len(nums) - 1
    pairs = [] 
    while left < right:
        par_sum = nums[left] + nums[right]
        if par_sum < target:
            left += 1
        elif par_sum > target:
            right -= 1
        else:
            pairs.append([nums[left], nums[right]])
            left += 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
    return pairs


"""
Complexity Analysis
The time complexity of triplet_sum is O(n^2)
- We first sort the array, which takes O(nlog(n))
- Then, for each of the n elements in the array, we call pair_sum_sorted_all
at most once, which runs in O(n) time.
Therefore, te overral complexity O(n^2)
"""

