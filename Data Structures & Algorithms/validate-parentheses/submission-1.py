class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chars = {'(':')', '[':']', '{':'}'}
        for i in s:
            if i in chars.values():
                if not stack:
                    return False
                else:
                   popped = stack.pop()
                   if chars[popped] != i:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0
