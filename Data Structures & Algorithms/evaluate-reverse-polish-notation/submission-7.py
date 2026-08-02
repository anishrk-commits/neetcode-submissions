class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for item in tokens:
            try:
                stack.append(int(item))
            except ValueError:
                second = stack.pop()
                first = stack.pop()
                if(item == "+"):
                    stack.append(first + second)
                elif(item == "-"):
                    stack.append(first - second)
                elif(item == "*"):
                    stack.append(first * second)
                else:
                    stack.append(int(first / second))
            print(stack)
        return stack[0]