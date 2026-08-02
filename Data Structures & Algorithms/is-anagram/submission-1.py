class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        seen = {}
        seen2 = {}

        if (len(s) != len(t)):
            return False
        for ch in s:
            if(ch in seen):
                seen[ch] += 1
            else:
                seen[ch] = 1
        
        for ch in t:
            if(ch in seen2):
                seen2[ch] += 1
            else:
                seen2[ch] = 1

        if(seen == seen2):
            return True
        else:
            return False