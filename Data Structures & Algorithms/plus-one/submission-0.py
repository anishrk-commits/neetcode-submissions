class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for i in digits:
            num = num + str(i)
        
        number = int(num)

        number += 1

        num = str(number)

        answer = []
        print(num)
        for i in num:
            answer.append(int(i))
        
        return answer