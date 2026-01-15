class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = []

        for i in strs:
            k = len(i)
            encodedString.append(str(k))
            encodedString.append("#")
            encodedString.append(i)

        encoded = "".join(encodedString)
        return encoded

    def decode(self, s: str) -> List[str]:
        decodedString = []
        i = 0
        k = ""
        
        while i < len(s):
            if s[i] != "#":
                k += s[i]
                i += 1
            elif s[i] == "#":
                count = int(k)
                string = s[i + 1: i + count + 1]
                i += count + 1
                decodedString.append(string)
                k = ""

        return decodedString

"""
Approach:
- Encode each string by prefixing it with its length and a delimiter ('#')
- Concatenate all encoded strings into a single string
- During decoding, read characters until the delimiter to get the length
- Use the length to extract the next substring and repeat

Time Complexity: O(n)
Space Complexity: O(n)
Difficulty: Medium
"""
