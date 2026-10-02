class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        answer = []
        freq = dict.fromkeys(arr2, 0)
        freq[-1] = []

        for num in arr1:
            if num in freq:
                freq[num] = freq.get(num, 0) + 1
            else:
                freq[-1].append(num)
        
        for num in arr2:
            for i in range(freq[num]):
                answer.append(num)
        if len(freq[-1]) > 0:
            freq[-1] = sorted(freq[-1])
            answer.extend(freq[-1])
        return answer


