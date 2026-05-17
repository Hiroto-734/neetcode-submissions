class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        res = {}

        while left < right:
            min_height = min(heights[left], heights[right])
            width = right - left
            area = min_height * width
            res[(left, right)] = area

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return max(res.values())