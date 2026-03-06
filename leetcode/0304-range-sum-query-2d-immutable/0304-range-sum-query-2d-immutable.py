class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rows, cols = len(matrix), len(matrix[0])
        #now build a prefix_sum matrixt 
        self.pref_sum = [[0]*cols for _ in range(rows)]

        for i in range(rows): 
            for j in range(cols): 
                left = self.pref_sum[i][j-1] if j > 0 else 0
                top = self.pref_sum[i-1][j] if i > 0 else 0 
                overlap = self.pref_sum[i-1][j-1] if i>0 and j>0 else 0


                self.pref_sum[i][j] = matrix[i][j] +  top + left  - overlap

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #find the start and end of the boxes from the queries 
        left = self.pref_sum[row2][col1-1] if col1 >0 else 0
        top = self.pref_sum[row1-1][col2] if row1 > 0 else 0
        overlap = self.pref_sum[row1-1][col1-1] if row1>0 and col1>0 else 0


        return self.pref_sum[row2][col2]-top-left+overlap 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)