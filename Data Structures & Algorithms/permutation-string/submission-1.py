class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
    
        frequency = {}
        for i in s1:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1
        
        tracker = {}
        for i in range(len(s1)):
            if s2[i] not in tracker:
                tracker[s2[i]] = 1
            else:
                tracker[s2[i]] += 1
        left = 0
        right = len(s1)
        while right < len(s2):
            if tracker == frequency:
                return True
            else:
                if s2[right] not in tracker:
                    tracker[s2[right]] = 1
                else:
                    tracker[s2[right]] += 1
                
                tracker[s2[left]] -= 1

                if tracker[s2[left]] == 0:
                    del tracker[s2[left]]

                left += 1
                right += 1

        if tracker == frequency:
                return True
        else:
            return False

