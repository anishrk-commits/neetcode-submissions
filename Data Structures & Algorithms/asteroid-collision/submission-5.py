from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = deque()
        broken = False
        for asteroid in asteroids:
            while stack:
                if not (asteroid < 0 and stack[-1] > 0):
                    break
                
                if abs(asteroid) > abs(stack[-1]):
                    stack.pop() 
                elif abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                    broken = True
                    break
                else:
                    broken = True
                    break
            if broken:
                broken = False
            else:
                stack.append(asteroid)
        return list(stack)
