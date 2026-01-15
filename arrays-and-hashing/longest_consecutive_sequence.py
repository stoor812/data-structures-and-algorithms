from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        exist = {}
        count = 1
        
        if len(nums) == 0: return 0

        # Store values that exist in hashmap 
        for n in nums:
            if n not in exist:
                exist[n] = 1

        for x in nums:
            if x - 1 in exist: # This is a middle element
                continue
            else: # This is the start of a sequence
                start = x
                newCount = 1
                while True:
                    if start + 1 in exist:
                        newCount += 1
                        start += 1
                    else: 
                        break
                if newCount > count:
                    count = newCount

        return count

"""
Approach:
- Store all numbers in a hash map for O(1) existence checks
- Iterate through the array and only start counting when the current number
  does not have a predecessor (x - 1 not in map)
- From each valid start, expand forward while consecutive numbers exist
- Track and return the maximum sequence length found

Time Complexity: O(n)
Space Complexity: O(n)
Difficulty: Medium
"""
