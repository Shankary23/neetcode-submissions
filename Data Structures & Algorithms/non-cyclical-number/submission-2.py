class Solution:
    def isHappy(self, n: int) -> bool:
        # num = str(n)
        tot = n
        # for i in num:
        #     tot += int(i)**2
        
        seen = set()
        while tot != 1:
            old = str(tot)
            tot = 0
            for i in old:
                tot += int(i)**2
            if tot in seen:
                return False
            else:
                seen.add(tot)
        return True




