class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stk = []
        for i in range(len(path)): 
            if path[i] == "..": 
                if stk: 
                    stk.pop()
            elif path[i] == "." or path[i] == "": 
                continue 
            else: 
                stk.append(path[i])
        
        return "/" + "/".join(stk)  