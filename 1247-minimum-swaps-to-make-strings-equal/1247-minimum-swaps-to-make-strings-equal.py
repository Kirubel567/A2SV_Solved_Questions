class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx = 0, 0 
        for i in range(len(s1)): 
            if s1[i] == "x" and s2[i] == 'y': 
                xy += 1
            if s1[i] == 'y' and s2[i] == 'x': 
                yx += 1
        if (xy+yx)%2: 
            return -1
        return xy//2 + yx//2 + (xy%2)*2