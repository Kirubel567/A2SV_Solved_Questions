class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #map the heights with the names 
        mapp = {}
        for i in range(len(names)): 
            mapp[heights[i]] = names[i]
        #sort the heights
        heights.sort(reverse=True)

        res = [0] * len(names)
        for i in range(len(heights)): 
            res[i] = mapp[heights[i]]

        return res
