class Solution:
    def romanToInt(self, s: str) -> int:
        #use a hash table to do this quesiton 
        mapp = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D":500, "M": 1000}

        Sum = 0
        for i in range(len(s) - 1): 
            if mapp[s[i]] >= mapp[s[i+1]]: 
                Sum += mapp[s[i]]
            elif mapp[s[i]] < mapp[s[i + 1]]: 
                Sum -= mapp[s[i]]

        Sum += mapp[s[len(s)-1]]
        return Sum 
