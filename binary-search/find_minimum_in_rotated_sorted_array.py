from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                # Search Right Part of the Array
                left = middle + 1
            elif nums[middle] < nums[right]:
                # Search Left Part of the Array
                right = middle
            else:
                return nums[middle]

        return nums[left]

"""
Approach:
- Use binary search on the rotated sorted array
- Compare the middle element with the rightmost element
- If nums[middle] > nums[right], the minimum lies in the right half
- If nums[middle] < nums[right], the minimum lies in the left half (including middle)
- Narrow the search space until left == right, which points to the minimum

Time Complexity: O(log n)
Space Complexity: O(1)
Difficulty: Medium
"""
