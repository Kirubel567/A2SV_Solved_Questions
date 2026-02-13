class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
    
        for i in range(rows):    
            image[i].reverse()

        for i in range(rows): 
            for j in range(cols): 
                if image[i][j] == 0: 
                    image[i][j] = 1
                else: 
                    image[i][j] = 0
                    
        return image