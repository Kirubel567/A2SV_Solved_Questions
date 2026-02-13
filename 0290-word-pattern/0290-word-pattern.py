class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapp = {}
        arr = s.split()
        if len(arr) != len(pattern): 
            return False
            
        for i in range(len(pattern)): 
            if pattern[i] in mapp and mapp[pattern[i]] != arr[i]: 
                return False 
            if arr[i] in mapp.values() and pattern[i] not in mapp: 
                return False
            mapp[pattern[i]] = arr[i]

        return True 
