class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = {}
        for number in nums:
            freq[number] = freq.get(number, 0) + 1
        
        return max(freq, key=freq.get)

            