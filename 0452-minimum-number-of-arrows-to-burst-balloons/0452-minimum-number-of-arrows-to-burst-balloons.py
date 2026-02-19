class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: [x[0], x[1]])
        if len(points) == 1: 
            return 1
        i = len(points)-1
        count, curr = 0, []
        while i > 0: 
            curr = points[i]
            while i > 0 and curr[0] <= points[i-1][1]: 
                i -= 1
            count += 1
            i-=1
        
        if not curr[0] <= points[0][1]: 
            count += 1
        return count 
