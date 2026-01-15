from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        sufix = deque()
        products = []

        # Init Prefix Product Array O(n)
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prod = prefix[i - 1] * nums[i]
                prefix.append(prod)

        # Init Suffix Product Array O(n)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                sufix.appendleft(nums[i])
            else:
                prod = sufix[0] * nums[i]
                sufix.appendleft(prod)
            
        for i in range(len(nums)):
            if i == 0: # First Element
                products.append(sufix[i + 1])
            elif i == len(nums) - 1: # Last Element
                products.append(prefix[i - 1])
            else:
                prod = sufix[i + 1] * prefix[i - 1]
                products.append(prod)

        return products
    
"""
Approach:
- Build a prefix product array where each index stores the product of all elements to the left
- Build a suffix product array where each index stores the product of all elements to the right
- For each index, multiply the corresponding prefix and suffix values to get the result
- Handle edge cases for the first and last elements separately

Time Complexity: O(n)
Space Complexity: O(n)
Difficulty: Medium
"""
