from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxProfit = 0

        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            profit = prices[right] - prices[left]
            maxProfit = max(profit, maxProfit)

        return maxProfit
    
"""
Approach:
- Use two pointers where `left` tracks the minimum price index (buy day)
- Iterate with `right` as the selling day
- If a lower price is found, move `left` to that index
- Compute profit as prices[right] - prices[left] and track the maximum profit

Time Complexity: O(n)
Space Complexity: O(1)
Difficulty: Easy
"""
