class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0]
        for par in s: 
            if par=="(": 
                stk.append(0)
            else: 
                val=max(2*stk.pop(), 1)
                stk[-1]+=val
        return stk[-1]