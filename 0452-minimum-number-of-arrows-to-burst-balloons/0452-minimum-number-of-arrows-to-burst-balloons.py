class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #if there ia an overlap between two coordinates then we need only one arrow
        #but inorder to compare the rest of the arrows we have to use the larger range
        points.sort(key=lambda x: [x[0], x[1]])
        #start from the end
        #check if the first element is lessthan or equal to the second element of the arr found before the current one 
        #use while loop to manipulate the iteration 
        #currMax = the maximum of the element[0] but this is already sorted
        if len(points) == 1: 
            return 1
        i = len(points)-1
        count, curr = 0, []
        while i > 0: 
            flag = True 
            curr = points[i]
            while i > 0 and curr[0] <= points[i-1][1]: 
                i -= 1
                flag = False 
            count += 1
            print(count)
            
            i-=1
        if not curr[0] <= points[0][1]: 
            count += 1
        
        print(points)
        return count 