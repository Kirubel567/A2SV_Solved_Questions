class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        for ch in s: 
            if stk and ch == "*": 
                stk.pop()
            else: 
                stk.append(ch)
        return "".join(stk)