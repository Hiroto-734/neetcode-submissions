from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        countS1 = Counter(s1)
        window = Counter(s2[:len(s1)])

        if countS1 == window:
            return True

        for i in range(len(s2) - len(s1)):
            window[s2[i]] -= 1
            window[s2[i+len(s1)]] += 1

            if window[s2[i]] == 0:
                del window[s2[i]] 
            
            if countS1 == window:
                return True
        
        return False