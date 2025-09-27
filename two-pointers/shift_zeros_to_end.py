"""
Shift Zeros to the End

Given an array of intergers, modify the array in place to move all zeros to
the end while maintaining the relative order of non-zero elements.

Input: nums = [0, 1, 0, 3, 2]
Output: [1, 3, 2, 0, 0]

Intuition
This problem has three main requirements:
1. Movel all zeros to the end of the array
2. Maintain the relative order of the non-zero elements
3. Perform the modification in place

This solution breaks the third requirement of modifying the input array 
in place.
"""
from typing import List

def shift_zeros_to_the_end_naive(nums: List[int]) -> None:
    temp = [0] * len(nums)
    i = 0
    for num in nums:
        if num != 0:
            temp[i] = num
            i += 1

    for j in range(len(nums)):
        nums[j] = temp[j]
        
"""
[0, 1, 0, 2, 3  ]
1 - [0, 1] --> [1, 0]
2 - [0, 0] --> 

Complexity Analysis

Time complexity --> is O(n) where n denotes the length of the array
Space complexity --> is O(1) because shifting is done in place
"""
def shift_zeros_to_the_end(nums: List[int]) -> None:
    left, right = 0, 0  
    for num in nums:
        if nums[right] == 0:
            right += 1
        elif nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1
        elif nums[left] == 0 and nums[right] == 0:
            right += 1

        

if __name__ == '__main__':
    
    nums = [0, 1, 0, 2, 3]

    shift_zeros_to_the_end(nums)

