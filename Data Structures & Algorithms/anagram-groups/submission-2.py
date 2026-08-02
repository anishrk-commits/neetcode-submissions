class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        tracker = []
        answer = []

        for word in strs:
            group = {}
            for ch in word:
                if ch not in group:
                    group[ch] = 1
                else:
                    group[ch] += 1

            if(group not in tracker):
                tracker.append(group)
                answer.append([word])
            else:
                answer[tracker.index(group)].append(word)
        return answer


    
        

