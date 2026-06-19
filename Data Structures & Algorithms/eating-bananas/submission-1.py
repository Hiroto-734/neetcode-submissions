class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)          # 答えの範囲

        def hours_needed(k):           # 速さ k で食べきるのにかかる時間
            return sum((pile + k - 1) // k for pile in piles)   # 君の切り上げ計算

        while l < r:
            mid = (l + r) // 2
            if hours_needed(mid) <= h:    # mid で間に合う
                r = mid                    # もっと遅くできるか試す（mid 自身も候補なので残す）
            else:                          # 間に合わない
                l = mid + 1                # もっと速く（mid は失格なので外す）
        return l