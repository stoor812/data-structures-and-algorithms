from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid

            # CASE 1 - Left Sorted Portion
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    # Search Right
                    left = mid + 1
                else:
                    right = mid - 1

            #CASE 2 - Right Sorted Portion
            elif nums[right] >= nums[mid]:
                if target > nums[mid] and target <= nums[right]:
                    # Search Right - mid < target <= right
                    left = mid + 1
                else:
                    right = mid - 1
        
        # TARGET NOT FOUND
        return -1

"""
Approach:
- Use modified binary search on the rotated sorted array
- At each step, determine which half (left or right) is sorted
- If the target lies within the sorted half, search there
- Otherwise, search the opposite half
- Continue until the target is found or the search space is exhausted

Time Complexity: O(log n)
Space Complexity: O(1)
Difficulty: Medium
"""


            
            
            





            
            

        