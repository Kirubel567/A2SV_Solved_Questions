class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, ans, window = 0, -float('inf'), 0
        count = defaultdict(int)

        for right in range(len(s)): 
            count[s[right]] += 1
            window += 1
            while window - max(count.values()) > k: 
                count[s[l]] -= 1
                l+= 1
                window -= 1
            ans = max(window, ans)
                
        return ans 