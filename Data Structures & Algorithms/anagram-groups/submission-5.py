class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for string in strs:
            counts = {}

            for char in string:
                counts[char] = counts.get(char, 0) + 1

            counts_tuple = tuple(sorted(counts.items()))

            if counts_tuple in answer:
                answer[counts_tuple].append(string)
            else:
                answer[counts_tuple] = [string]
    
        answer_strings = []
        for key, value in answer.items():
            answer_strings.append(value)
        
        return answer_strings

       