class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        res = []

        def backtrack(path):
            if len(res) == k:
                return
        
            if len(path) == n:
                res.append(path)
                return
            
            for ch in ['a', 'b', 'c']:
                if not path or path[-1] != ch:
                    backtrack(path + ch)

        backtrack("")
        
        return res[k - 1] if k <= len(res) else ""