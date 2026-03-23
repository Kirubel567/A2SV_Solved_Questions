class Solution:
    def kthCharacter(self, k: int) -> str:
        st = "a"
        def recur():
            nonlocal st
            if len(st) >= k: 
                return 
            
            _new = []
            for i in range(len(st)): 
                _new.append(chr(ord(st[i])+1))

            st += "".join(_new)
            recur()

        recur()
        return st[k-1]


