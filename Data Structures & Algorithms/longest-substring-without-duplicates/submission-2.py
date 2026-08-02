class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        reference = set()

        left = 0
        right = 1

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        longest = 0
        reference.add(s[left])
        while right < len(s):
            if s[right] not in reference:
                reference.add(s[right])
                right += 1
                if right - left > longest:
                    longest = right - left
            else:
                while True:
                    reference.remove(s[left])
                    left += 1
                    if left == right:
                        break
                    elif s[right] in reference:
                        continue
                    else:
                        break
        return longest
        




