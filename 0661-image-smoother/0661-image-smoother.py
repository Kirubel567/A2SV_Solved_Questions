class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        res = [[0]*cols for _ in range(rows)]


        for r in range(rows): 
            for c in range(cols): 
                Sum, count = 0, 0 

                for row in range(max(r-1, 0), min(rows,r+2)): 
                    for col in range(max(0,c-1), min(c+2, cols)): 
                        # if row < 0 or row>=rows or col < 0 or col>=cols: 
                        #     continue 
                        Sum += img[row][col]
                        count += 1
                
                avg = Sum // count 
                res[r][c] = avg 
        
        return res 
        