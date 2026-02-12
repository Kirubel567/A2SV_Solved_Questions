class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq1 = Counter(ransomNote)
        freq2 = Counter(magazine)

        for key in freq1: 
            if key not in freq2 or freq2.get(key, 0) < freq1.get(key, 0): 
                return False 
        
        return True 