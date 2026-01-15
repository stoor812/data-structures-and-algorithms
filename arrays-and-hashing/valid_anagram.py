class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}

        for char in s:
            if char in hash_s:
                hash_s[char] += 1
            else:
                hash_s[char] = 1
        
        for char in t:
            if char in hash_t:
                hash_t[char] += 1
            else:
                hash_t[char] = 1

        return hash_s == hash_t

"""
Approach:
- Use two hash maps to count character frequencies for each string
- Iterate through both strings and populate their respective maps
- Compare the two hash maps for equality

Time Complexity: O(n)
Space Complexity: O(n)
Difficulty: Easy
"""
