class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        count = {}
        for number in nums:
            count[number] = count.get(number, 0) + 1
        
        reverse = {}
        for number, freq in count.items():
            if freq not in reverse:
                reverse[freq] = [number]
            else:
                reverse[freq].append(number)
        
        max_len = len(nums)
        while  max_len > 0:
            if max_len in reverse:
                answer.extend(reverse[max_len])
                k -= len(reverse[max_len])
            
            if k <= 0:
                break
            
            max_len -= 1
        return answer
