class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = []
       
        product = 1
        zero_count = 0
        for number in nums:
            if number == 0:
                zero_count += 1
                continue
            product *= number

        

        for number in nums:
            if zero_count > 1:
                answer.append(0)
            elif zero_count == 1 and number != 0:
                answer.append(0)
            elif zero_count == 1 and number == 0:
                answer.append(int(product))
            else:
                answer.append(int(product / number))
        
        return answer


        