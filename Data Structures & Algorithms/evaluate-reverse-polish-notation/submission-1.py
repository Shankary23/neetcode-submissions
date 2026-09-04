class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = []
        res = 0

        for i in tokens:
            if i == "+" and symbols:
                first = symbols.pop()
                second = symbols.pop()
                res = (first) + (second)
                symbols.append(res)
            elif i == "*" and symbols:
                first = symbols.pop()
                second = symbols.pop()
                res = (first) * (second)
                symbols.append(res)  
            elif i == "-":
                first = symbols.pop()
                second = symbols.pop()
                res = (second) - (first)
                symbols.append(res)
            elif i == "/":
                first = symbols.pop()
                second = symbols.pop()
                res = int((second)/(first))
                symbols.append(res)
            else:
                symbols.append(int(i))
        return symbols[0]
