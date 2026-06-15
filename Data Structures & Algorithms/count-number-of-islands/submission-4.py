class Solution:

   

    def dfs(self, grid, r,c):
        grid[r][c]= '0'
        directions_lst = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
        for row,col in directions_lst:
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[row]) and grid[row][col] =='1':
                self.dfs(grid,row,col)

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    self.dfs(grid,r,c)
                    islands += 1
        return islands


    #     # if not grid :
        #     return 0 
        
        # rows, cols = len(grid),len(grid[0])
        # visited = set()
        # island = 0

        # def bfs(r,c):
        #     q = collections.deque()
        #     visited.add((r,c))
        #     q.append((r,c))
        #     while q :
        #         row,col = q.popleft()
        #         directions = [[1,0],[-1,0],[0,1],[0,-1]]
        #         for dr , dc in directions:
        #             r,c = row + dr , col + dc 

        #             if (r in range(rows ) and 
        #                 c in range(cols) and 
        #                 grid[r][c] == "1" and 
        #                 (r, c) not in visited):
        #                     q.append((r,c))
        #                     visited.add((r,c))

        # for r in range(rows):
        #     for c in range(cols):
        #         if  grid[r][c] =="1" and (r,c) not in visited :
        #             bfs(r,c)
        #             island += 1
        #     return island

    
