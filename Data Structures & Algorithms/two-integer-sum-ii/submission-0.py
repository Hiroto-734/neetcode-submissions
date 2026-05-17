class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res =[]
        seen = {}
        for i,x in enumerate(numbers):
            diff = target - x
            if diff in seen:
                res.append(seen[diff])
                res.append(i+1)
                return res
            seen[x] = i+1
        return []
