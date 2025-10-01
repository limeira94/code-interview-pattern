"""
Longest Chain of Consecutive Numbers

Find the longest chain of consecutive numbers in an array. Two numbers are
consecutive if they have a different of 1.

Input: nums = [1, 6, 2, 5, 8, 7, 10, 3]
Output: 4

Explanation -> 5, 6, 7, 8

This brute force approach takes O(n^3) time because of the nested operation involved:
- for loop iterates to each element
- n intereations for each element
- while loop
"""

from typing import List


def longest_chain_of_consecutive_numbers_brute_froce(nums: List[int]) -> int:
    if not nums:
        return 0

    longest_chain = 0
    for num in nums:
        current_num = num
        current_chain = 1
        while current_num + 1 in nums:
            current_num += 1
            current_chain += 1
        longest_chain = max(longest_chain, current_chain)
    return longest_chain


"""
Optimization - identifying the start of each chain
- checking the array doesn't contain the number that precedes it (curr_num - 1)
nums = [1, 6, 2, 5, 8, 7, 10, 3]

Time complexity -> O(n)
Space complexity -> O(n)
"""

def longest_chain_of_consecutive_numbers(nums: List[int]) -> int:
    if not nums:
        return 0
    
    num_set = set(nums)
    longest_chain = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_chain = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_chain += 1
            
            longest_chain = max(longest_chain, current_chain)
    
    return longest_chain

# if __name__ == "__main__":
#     nums = [1, 6, 2, 5, 8, 7, 10, 3]

#     longest_chain_of_consecutive_numbers_brute_froce(nums)

