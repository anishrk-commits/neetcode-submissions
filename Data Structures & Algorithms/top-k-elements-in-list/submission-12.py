class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for number in nums:
            count[number] = count.get(number, 0) + 1
        
        reverse = {}
        for number, count in count.items():
            if count not in reverse:
                reverse[count] = [number]
            else:
                reverse[count].append(number)
        
        answer = []
        for freq in range(len(nums), 0, -1):
            if freq in reverse:
                answer.extend(reverse[freq])
            if len(answer) == k:
                return answer


