class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counter = {}
        longest = 0
        left = 0

        for i in range(len(s)):
            right = i
            if s[i] in counter:
                counter[s[i]] += 1
            else:
                counter[s[i]] = 1


            most_freq = max(counter.values())

            if most_freq + k >= right - left + 1:
                longest = right - left + 1
            else:
                counter[s[left]] -= 1
                left += 1

        return longest

        
