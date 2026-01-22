class TimeMap:

    def __init__(self):
        self.hash = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            self.hash[key] = []
        self.hash[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash:
            return ""
        elif timestamp < self.hash[key][0][0]:
            return ""
        else:
            # Binary Search 
            lst = self.hash[key]
            left = 0
            right = len(lst) - 1
            max = 0

            while left <= right:
                mid = (left + right) // 2

                if timestamp < lst[mid][0]: # Search Left
                    right = mid - 1
                elif timestamp >= lst[mid][0]: # Search Right
                    max = mid
                    left = mid + 1

            return lst[max][1]
        
"""
Approach:
- Use a hash map where each key maps to a list of (timestamp, value) pairs
- Append values in increasing timestamp order during set operations
- For get operations, perform binary search on the timestamp list for the given key
- Find the largest timestamp less than or equal to the query timestamp
- Return the corresponding value, or an empty string if no valid timestamp exists

Time Complexity:
- set: O(1)
- get: O(log n), where n is the number of values stored for the key
Space Complexity: O(n)
Difficulty: Medium
"""


        
