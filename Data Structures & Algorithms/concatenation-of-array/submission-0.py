class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = [""] * (2 * len(nums))

        j = 0
        for i in nums:
            ans[j] = i
            ans[j + len(nums)] = i
            j += 1
        return ans
