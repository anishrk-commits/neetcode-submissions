class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        shortest = min(strs)
        for i in range(len(shortest)):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return answer
            answer += strs[0][i]
        
        return answer