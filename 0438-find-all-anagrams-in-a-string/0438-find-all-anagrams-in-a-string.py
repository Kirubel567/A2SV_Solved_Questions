class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_p = Counter(p)
        count_s = Counter(s[:len(p)])
        left = 0
        ans = []

        if count_s == count_p: 
            ans.append(left)

        for r in range(len(p), len(s)): 
            count_s[s[r]] += 1
            count_s[s[left]] -= 1
            left+=1

            if count_s == count_p: 
                ans.append(left)
            
    
        return ans