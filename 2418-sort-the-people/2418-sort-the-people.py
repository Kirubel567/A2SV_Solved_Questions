class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mapp = {}
        ans = []
        for i in range(len(heights)): 
            mapp[heights[i]] = names[i]

        for i in range(len(heights)): 
            for j in range(i+1, len(heights)): 
                if heights[i] < heights[j]: 
                    heights[i], heights[j] = heights[j], heights[i]
        print(heights)
        for h in heights: 
            ans.append(mapp[h])
        
        return ans 
