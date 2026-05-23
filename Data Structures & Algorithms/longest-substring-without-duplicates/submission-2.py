class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        n = len(s)

        slow, fast = 0, 0

        while fast < n:
            if s[fast] not in s[slow:fast]:
                fast += 1
            else:
                slow += 1
            maxLength = max(fast - slow, maxLength)
        
        return maxLength




