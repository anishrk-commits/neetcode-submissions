class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = {}

        for number in nums:
            if number not in frequency:
                frequency[number] = 1
            else:
                frequency[number] += 1
        
        # print(frequency)

        invert = {}

        for key, value in frequency.items():
            if value not in invert:
                invert[value] = [key]
            else:
                invert[value].append(key)
        print(invert)
        place = 0
        answer = []
        
        for i in range(len(nums), -1, -1):
            if(place == k):
                    return answer
            if(i in invert):
                answer.extend(invert[i])
                place += len(invert[i])

        
        return 1
        
