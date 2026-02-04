class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left = 0
        maxFreq = 0
        maxLen = 0

        for right in range(len(s)):
            window = (right - left) + 1
            x = s[right]

            # Add Char to Hashmap
            if x not in hashmap:
                hashmap[x] = 1
            else:
                hashmap[x] += 1
            # Check for Highest Frequency
            maxFreq = max(hashmap[x], maxFreq)

            # Shrink Window
            while window - maxFreq > k:
                #Reduce Freq
                hashmap[s[left]] -= 1
                left += 1
                window = (right - left) + 1

            maxLen = max(maxLen, window)

        return maxLen

"""
Approach:
- Use a sliding window with left and right pointers
- Maintain a hash map to count character frequencies in the window
- Track the maximum frequency of any character seen in the window
- If (window size - max frequency) > k, shrink the window from the left
- Update and return the maximum valid window length

Time Complexity: O(n)
Space Complexity: O(n)
Difficulty: Medium
"""
