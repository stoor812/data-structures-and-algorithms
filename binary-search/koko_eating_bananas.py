from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        minK = right

        while left <= right:
            middle = (left + right) // 2
            result = self.validHelper(piles, middle, h)

            if result == 1:
                # Valid so Check Lower
                minK = middle
                right = middle - 1
            elif result == -1:
                # Not Valid so Check Higher
                left = middle + 1

        return minK


    def validHelper(self, piles: List[int], k: int, h: int) -> int:
        count = 0

        for i in piles:
            time = i // k
            extraTime = i % k
            count += time
            if extraTime != 0: count += 1
        
        if count <= h:
            return 1
        elif count > h:
            return -1

"""
Approach:
- Use binary search on the possible eating speeds (k)
- Search range is from 1 to max(piles)
- For each candidate speed, calculate total hours needed using a helper function
- If total hours <= h, the speed is valid; try to find a smaller valid speed
- If total hours > h, increase the speed
- Return the minimum valid eating speed found

Time Complexity: O(n log m)
  - n = number of piles
  - m = maximum pile size
Space Complexity: O(1)
Difficulty: Medium
"""        