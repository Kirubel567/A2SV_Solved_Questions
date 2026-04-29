class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=0
        minutes = 0
        queue = deque()


        #we ain't using adj array just the grid itself
        def inbound(r, c): 
            return 0<=r<len(grid) and 0<=c<len(grid[0])

        #now count fresshes and append the sources(the rotten ones) to the queue 
        for r in range(len(grid)): 
            for c in range(len(grid[0])): 
                cell = grid[r][c]
                if cell == 2: 
                    queue.append((r,c))
                if cell == 1: 
                    fresh+=1
        
        #determine the allowed movements in the grid 
        directions = [(1, 0), (0,1), (-1,0), (0, -1)]

        #now continut with the bfs 
        while queue: 
            for _ in range(len(queue)): #to move level by level
                cr, cc = queue.popleft()

                for ar, ac in directions: 
                    nr, nc = cr+ar, cc+ac

                    if not inbound(nr, nc): continue
                    if grid[nr][nc] != 1: continue 
                    grid[nr][nc] = 2

                    fresh-=1
                    queue.append((nr, nc))
                
            minutes += 1



        if fresh >0: 
            return -1
        else: 
            return max(0, minutes-1)      