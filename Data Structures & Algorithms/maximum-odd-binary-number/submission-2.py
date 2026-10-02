class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        freq = {}

        for char in s:
            freq[int(char)] = freq.get(int(char) , 0) + 1
        
        answer = ""
        answer += "1" * (freq[1] - 1)
        if freq[1] != len(s):
            answer += "0" * (freq[0])
        answer += "1"

        return answer