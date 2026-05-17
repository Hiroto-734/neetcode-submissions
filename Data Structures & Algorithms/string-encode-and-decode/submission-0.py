class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for chs in strs:
            res += str(len(chs)) + "#" + chs
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+length+1])
            # 5#Hello9# i=0, j=1, length = 5
            i = j + length + 1
        return res
