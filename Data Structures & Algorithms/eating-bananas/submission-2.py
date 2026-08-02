import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        while left <= right:
            middle = (left + right) // 2

            k = 0
            for bananas in piles:
                k += math.ceil(bananas/middle)
                

            if h == k:
                right = middle - 1
            elif k < h:
                right = middle - 1
            else:
                left = middle + 1

        return left
