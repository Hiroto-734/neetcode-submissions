class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        cal = []
        operator = ['+', '-', '*', '/']
        for idx, ch in enumerate(tokens):
            
            if ch in operator:
                if ch == '+':
                    res = cal[-2] + cal[-1]
                elif ch == '-':
                    res = cal[-2] - cal[-1]
                elif ch == '*':
                    res = cal[-2] * cal[-1]
                elif ch == '/':
                    res = int(cal[-2] / cal[-1])
                
                del cal[-1]
                del cal[-1]

                cal.append(res)
            else:
                cal.append(int(ch))
        
        return cal[0]