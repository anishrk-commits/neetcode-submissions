class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}

        for string in strs:
            counts = [0] * 26

            for char in string:
                counts[ord(char) - ord('a')] += 1

            key = tuple(counts)

            if key in answer:
                answer[key].append(string)
            else:
                answer[key] = [string]

        return list(answer.values())