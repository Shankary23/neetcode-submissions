class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
            if i[-4] == "6" and i[-3] > "0":
                count+=1
            elif i[-4] > "6":
                count+=1
        return count
            