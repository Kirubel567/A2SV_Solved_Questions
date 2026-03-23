class Solution:
    def kthCharacter(self, k: int) -> str:
        def recur(st): 
            if len(st) >= k: 
                return st
            
            _num = []
            for i in range(len(st)): 
                _num.append(chr(ord(st[i])+1))
            return recur(st + "".join(_num))


        return recur("a")[k-1]