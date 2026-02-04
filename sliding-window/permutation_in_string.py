class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        k = len(s1)
        hashS1 = {}
        hashS2 = {}

        if len(s1) > len(s2): return False
        
        # Add S1 to hash
        for i in s1:
            if i not in hashS1:
                hashS1[i] = 1
            else:
                hashS1[i] += 1
        
        for right in range(len(s2)):
            window = (right - left) + 1
            x = s2[left]
            y = s2[right]

            # Add Right to Hash
            hashS2[y] = hashS2.get(y, 0) + 1

            if window == k:
                if hashS1 == hashS2: return True
            elif window > k: # Decrement Left
                hashS2[x] -= 1
                left += 1
                if hashS2[x] == 0: del hashS2[x]
                if hashS1 == hashS2: return True
        
        return False

"""
Approach:
- Use a fixed-size sliding window of length len(s1) over s2
- Build a frequency hash map for s1
- Slide the window across s2 while maintaining a frequency hash map for the window
- Compare the two hash maps at each valid window position
- If the maps match, a permutation of s1 exists in s2

Time Complexity: O(n)
Space Complexity: O(1)
Difficulty: Medium
"""

 

