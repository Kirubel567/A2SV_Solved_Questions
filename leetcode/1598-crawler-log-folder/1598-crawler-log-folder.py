class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []
        for folder in logs: 
            if folder == "../": 
                if stk: stk.pop()  
            elif folder == "./": 
                continue 
            else: 
                stk.append(folder)
        
        return len(stk)
