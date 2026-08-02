class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0

        reference = set()

        if len(s) == 1:
            return 1
        
        length = 0
        max = 0
        while right < len(s):
            if s[right] not in reference:
                reference.add(s[right])
                length += 1
                right += 1
            else:
                reference.remove(s[left])
                left += 1
                length += -1
            if length > max:
                max = length
        
        return max



