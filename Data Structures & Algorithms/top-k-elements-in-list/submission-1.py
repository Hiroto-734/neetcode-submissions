class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            count[x] = 1 + count.get(x, 0)

        freq = defaultdict(list)
        for key, value in count.items():
            freq[value].append(key)

        freq_list = sorted(freq.keys())
        res = []
        for i in range(len(freq_list)-1, -1, -1):
            frequency = freq_list[i]
            for j in freq[frequency]:
                res.append(j)
                if len(res) == k:
                    return res
        
        return res
        