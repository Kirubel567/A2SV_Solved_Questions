class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        stk = []
        for i in range(len(s)): 
            if s[i] == "(": 
                stk.append(score)
                score = 0
            else: 
                score = stk.pop() + max(score*2, 1)
            
        return score 
