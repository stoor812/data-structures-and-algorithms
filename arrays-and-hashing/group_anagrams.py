from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for word in strs: # Loop through each word in List
            count = [0] * 26 
            for s in word: # Loop through each char in Word
                index = ord(s) - ord('a')
                count[index] += 1
            # Create Key & Add to HashMap
            key = tuple(count)
            if key not in hashmap:
                hashmap[key] = [word]
            else:
                hashmap[key].append(word)

        return list(hashmap.values())
        
"""
Approach:
- Use a hash map to group words by character frequency
- For each word, build a fixed-size count array of 26 letters
- Convert the count array to a tuple to use as a hashable key
- Append words with the same key into the same group

Time Complexity: O(n * k)
Space Complexity: O(n * k)
Difficulty: Medium
"""
