class Solution:
    def isValid(self, s: str) -> bool:
        
        open_char_list = ['(', '{', '[']
        close_char_list = [')', '}', ']']
        open_close_pair = {'(':')', '{':'}', '[': ']'}

        seen = []
        for ch in s:
            if ch in open_char_list:
                seen.append(ch)
            elif ch in close_char_list and seen:
                if ch == open_close_pair[seen[-1]]:
                    del seen[-1]
                else:
                    return False
            else:
                return False
        
        return not seen
        