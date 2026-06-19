class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        for i in range(1, len(temperatures)):
            for j in range(i):
                if res[j] == 0 and temperatures[i] > temperatures[j]:
                    res[j] = i - j
        return res