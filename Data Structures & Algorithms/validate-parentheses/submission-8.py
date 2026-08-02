class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []


        for item in s:
            if item == "[" or item == '{' or item == "(":
                stack.append(item)
            elif (item == "]" or item == '}' or item == ")") and len(stack) > 0:
                top = stack.pop()
                if top == "[" and item == "]":
                    continue
                elif top == "{" and item == "}":
                    continue
                elif top == "(" and item == ")":
                    continue
                else:
                    return False
            else:
                return False
        
        if(len(stack) != 0):
            return False
        return True

