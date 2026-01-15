
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