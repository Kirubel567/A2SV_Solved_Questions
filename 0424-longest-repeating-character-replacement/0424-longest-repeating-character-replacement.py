class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, ans = 0, -float('inf')
        counter = [0]*26

        for r in range(len(s)): 
            counter[ord(s[r])-ord('A')] += 1
            
            while (r-l+1) - max(counter) > k: 
                counter[ord(s[l])-ord('A')]-=1
                l+=1
            
            ans = max(ans, r-l+1)
        return ans 