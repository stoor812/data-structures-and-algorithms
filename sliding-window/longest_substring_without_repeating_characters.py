class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLen = 0
        elements = set()

        for right in range(len(s)):
            if s[right] not in elements: # DNE in set
                elements.add(s[right]) # Add to set
                maxLen = max(len(elements), maxLen)
            else: # Exists in set
                while s[right] in elements:
                    elements.remove(s[left])
                    left += 1
                elements.add(s[right])
                maxLen = max(len(elements), maxLen)

        return maxLen
    
"""
Approach:
- Use a sliding window with two pointers (left and right)
- Maintain a set to store unique characters in the current window
- Expand the window by moving `right` when the character is not in the set
- If a duplicate is found, shrink the window from the left until it is removed
- Track the maximum window size encountered

Time Complexity: O(n)
Space Complexity: O(n)
Difficulty: Medium
"""
