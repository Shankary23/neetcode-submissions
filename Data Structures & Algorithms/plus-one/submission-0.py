class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for i in digits:
            string += str(i)
        num = int(string)
        num +=1
        num = str(num)
        res = []
        for i in num:
            res.append(int(i))
        return res

