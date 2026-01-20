from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                # Search Right of Middle
                left = middle + 1
            elif nums[middle] > target:
                # Search Left of Middle
                right = middle - 1
            else:
                return middle
            
        return -1

"""
Approach:
- Maintain left and right pointers over the sorted array
- Repeatedly compute the middle index
- Compare the middle element with the target
- Narrow the search space by moving left or right accordingly
- Return the index if found, otherwise return -1

Time Complexity: O(log n)
Space Complexity: O(1)
Difficulty: Easy
"""
