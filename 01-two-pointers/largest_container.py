"""
Largest Container

You are given an array of numbers, each representing the height of a vertical
line on a graph. A container can be formed with any pair of these lines, along
with the x-axis of the graph. Return the amount of water which the largest
container can hold.

Input: heights: [2, 7, 8, 3, 7, 6]
Output: 24

1.  water = min(2,7)*(1-0) --> 2
2.  water = min(7,8)*(2-0) --> 14
3.  water = min(8,3)*(3-0) --> 9
4.  water = min(3,7)*(4-0) --> 12
            ...
"""

from typing import List


def largest_container_brute_force(heights: List[int]) -> int:
    n = len(heights)
    max_water = 0
    for i in range(n):
        for j in range(i + 1, n):
            water = min(heights[i], heights[j]) * (j - i)
            max_water = max(max_water, water)
    return max_water


"""
Searching through all possible pairs values takes O(n^2) time
"""

"""
Based on the decisions taken in the example, we can summarize the logic:
1. If the left line is smaller left += 1
2. If the right line is smaller right -= 1
3. If both lines have the same height, move both pointer inward.
[2, 7, 8, 3, 7, 6]
"""


def largest_container(heights: List[int]) -> int:
    max_water = 0
    left, right = 0, len(heights) - 1
    while left < right:
        water = min(heights[left], heights[right]) * (right - left)
        max_water = max(max_water, water)
        if heights[left] == heights[right]:
            left += 1
            right -= 1
        elif heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_water

"""
Complexity Analysis

Time complexity: is O(n) because we perform approximately n interations
using the two-pointer technique
Space complexity: We only allocated a constant number of variables, so the space
complexity is O(1)
"""