class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        rows, cols = len(mat), len(mat[0])
        for i in range(4):
            for i in range(rows): 
                for j in range(i, cols): 
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            for r in mat:
                r.reverse()
            if mat == target: 
                return True 
        return False 