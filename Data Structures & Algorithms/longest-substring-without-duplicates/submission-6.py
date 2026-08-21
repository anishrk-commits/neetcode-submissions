class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0

        max_len = right - left
        seen = set()
        while right < len(s):
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
            else:
                seen.add(s[right])
                right += 1
            
            curr_len = right - left

            if curr_len > max_len:
                max_len = curr_len
        return max_len