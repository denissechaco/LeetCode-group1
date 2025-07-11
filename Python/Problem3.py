#### LENGTH OF LONGEST SUBSTRING #####

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We will use a set to store unique characters in the current window
        seen = set()     
        # Start of the window 
        left = 0  
        #length of the longest substring found        
        max_length = 0    

        for right in range(len(s)):
            # If character is already in the set, shrink the window from the left
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add the current character and update max_length
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
