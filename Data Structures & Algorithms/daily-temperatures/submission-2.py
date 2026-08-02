class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        results = [0] * len(temperatures)

        for day in range(len(temperatures)):
            if day == 0:
                stack.append([temperatures[day], day])
                continue
            #print(stack)
            if temperatures[day] <= temperatures[day - 1]:
                stack.append([temperatures[day], day])
            else:
                while True:

                    if len(stack) == 0:
                        break
                    prev = stack.pop()

                    if temperatures[day] > prev[0]:
                        results[prev[1]] = day - prev[1]
                    else:
                        stack.append(prev)
                        break
                stack.append([temperatures[day], day])
        return results
                

            

        