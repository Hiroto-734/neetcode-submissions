class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = [0] * 26          # s1 の各文字の個数
        window = [0] * 26        # 今の窓の各文字の個数
        for c in s1:
            need[ord(c) - ord('a')] += 1
        for c in s2[:len(s1)]:
            window[ord(c) - ord('a')] += 1

        matches = sum(1 for i in range(26) if need[i] == window[i])

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # 右端を入れる
            ir = ord(s2[r]) - ord('a')
            window[ir] += 1
            if window[ir] == need[ir]:
                matches += 1                 # 一致するようになった
            elif window[ir] == need[ir] + 1:
                matches -= 1                 # 一致を1つ通り過ぎて壊した

            # 左端を出す
            il = ord(s2[l]) - ord('a')
            window[il] -= 1
            if window[il] == need[il]:
                matches += 1
            elif window[il] == need[il] - 1:
                matches -= 1
            l += 1

        return matches == 26