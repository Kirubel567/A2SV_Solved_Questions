class Solution:
    def customSortString(self, order: str, s: str) -> str:
        #count the freq of the order string 
        #based on that populate the output string 
        freq = Counter(s)

        ans = [""] * len(s)
        not_inc = []
        for i in range(len(order)): 
            ans.extend([order[i]] * freq[order[i]])
        not_inc = [ss for ss in s if ss not in order]

        return "".join(ans) + "".join(not_inc)
            
        
