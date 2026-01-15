from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for n in nums:
            if n in hash_map:
                # value already exists
                return True
            else:
                # add value to hashmap
                hash_map[n] = 1
        return False

"""
Approach:
- Iterate through the array once
- Use a hash map to track values seen so far
- If a value already exists in the map, return True
- If the loop completes, return False

Time Complexity: O(n)
Space Complexity: O(n)
Difficulty: Easy
"""