class Solution:

    def encode(self, strs: List[str]) -> str:
        return "$".join(strs)
    def decode(self, s: str) -> List[str]:
        res = []
        word = ""
        for i in range(len(s)):
            if s[i] != "$":
                word += s[i]
                print(word)
            elif s[i] == "$":
                res.append(word)
                word = ""
        if word != "":
            res.append(word)
        return res



        
