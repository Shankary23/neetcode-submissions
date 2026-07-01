class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chars = {'(':')', '[':']', '{':'}'}

        for i in s:
            if i in chars:
                stack.append(i)
            if i in stack:
                stack.pop()
        return len(stack) == 0

