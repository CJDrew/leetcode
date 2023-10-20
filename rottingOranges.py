import queue

def orangesRotting(grid):
        seen = set()
        que = queue.Queue()
        level = 0

        xLimit = len(grid[0])-1
        yLimit = len(grid)-1

        #get initial set of rotten oranges
        for y in range(yLimit+1):
            for x in range(xLimit+1):
                if grid[y][x] == 2:
                    que.put([y,x])
                    grid[y][x] = 1
        
        while not que.empty():
            cur = que.get()
            curx, cury = cur[1], cur[0]

            if not grid[cury][curx] != 1 and not (cury, curx) in seen:
                #set to rotten
                grid[cury][curx] = 2
                seen.add((cury,curx))

                #add all neighbors
                if cury > 0:
                    que.put([cury-1,curx])
                if curx > 0:
                    que.put([cury,curx-1])
                if cury < yLimit:
                    que.put([cury+1,curx])
                if curx < xLimit:
                    que.put([cury,curx+1])
                level += 1

        if any(1 in xRow for xRow in grid):
            return -1
        
        return level

orangesRotting([[2,1,1],[1,1,0],[0,1,1]])