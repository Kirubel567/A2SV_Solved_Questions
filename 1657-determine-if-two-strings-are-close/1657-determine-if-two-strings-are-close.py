class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #use array for freq counting as the two words might have different lengths 
        freq1 = [0]*26
        freq2 = [0]*26

        for ch in word1: 
            freq1[ord(ch) - ord("a")] += 1
        for ch in word2: 
            freq2[ord(ch)-ord("a")] += 1

        # freq1 = [2, 3, 1, 0, 0, ...]
        # freq2 = [1, 2, 3, 0, 0, ...]

        #check if the frequency of each word is the same 
        for i in range(26): 
            if freq1[i] == 0 and freq2[i] != 0 or freq1[i] != 0 and freq2[i] == 0:
                return False
        
        #check if a frequency  count is also presnt in the other 
        #eg. if counter (freq) 3 occurs check in word2 if there is a frequency of 3 not the key but the value 
        freq1.sort()
        freq2.sort()
        for i in range(26): 
            if freq1[i] != freq2[i]: 
                return False 
        
        return True 