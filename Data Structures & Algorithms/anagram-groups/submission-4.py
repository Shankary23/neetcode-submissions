class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for i in strs:
            ordered = ''.join(sorted(i))
            if ordered in groups:
                groups[ordered].append(i)
            else:
                groups[ordered] = [i]
        # res = sorted(groups.values(),key=len)
        # print(res)
        res = list(groups.values())
        return res
        
        