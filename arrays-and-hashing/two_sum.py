from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for n in range(len(nums)):
            hash_map[nums[n]] = n

        for n in range(len(nums)):
            complement = target - nums[n]
            if complement in hash_map:
                if n != hash_map[complement]:
                    return [n, hash_map[complement]]

"""
Approach:
- First pass: store each number and its index in a hash map
- Second pass: for each number, check if its complement exists in the map
- Ensure the same index is not used twice before returning the result

Time Complexity: O(n)
Space Complexity: O(n)
Difficulty: Easy
"""
