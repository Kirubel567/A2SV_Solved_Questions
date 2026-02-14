class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        sorted_string = sorted(freq,key=freq.get, reverse=True)
        ans = []
        for ch in sorted_string: 
            ans.append(ch*freq[ch])
        
        return "".join(ans)
        