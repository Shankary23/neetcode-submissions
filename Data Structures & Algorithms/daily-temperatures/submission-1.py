class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures)):
            # print(stack)
            # print(res)
            if stack:
                # print(stack[-1][0])
                # print(temperatures[i])
                while stack and stack[-1][0] < temperatures[i]:
                    # print("append")
                    res[stack[-1][1]] = (i - stack[-1][1])
                    stack.pop()
            
            stack.append((temperatures[i],i))
        return res

