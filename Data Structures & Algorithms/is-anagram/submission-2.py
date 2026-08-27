class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        t_chars = {}
        for char in s: 
            s_chars[char] = 1 + s_chars.get(char, 0)
        
        for char in t:
            t_chars[char] = 1 + t_chars.get(char,0)
        
        return t_chars == s_chars
        