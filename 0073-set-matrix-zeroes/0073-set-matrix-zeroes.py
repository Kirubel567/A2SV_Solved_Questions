class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        copy = [row[:] for row in matrix]

        
        for r in range(rows): 
            for c in range(cols): 

                if copy[r][c] == 0: 
                    for col in range(cols):
                        matrix[r][col] = 0
                    for row in range(rows): 
                        matrix[row][c] = 0

       