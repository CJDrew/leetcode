def uniquePaths(self, m: int, n: int) -> int:
        #Basic dfs is too slow. Cache results for each cell so I don't recompute
        cache = [[-1 for i in range(m)] for j in range(n)]
        ans = 0
        def dfs(x,y):
            nonlocal ans
            #Out of bounds. Kill the branch
            if x > m-1 or y > n-1:
                return 0
            #Check the cache and see if we can end early
            if cache[y][x] != -1:
                return cache[y][x]
            #We found the corner. Increment our answer
            elif x == m-1 and y == n-1:
                return 1
            #Still on our journey. Create a branch for right and another for down and cache results
            else:
                ans = dfs(x+1, y) + dfs(x, y+1)
                cache[y][x] = ans
                return ans
        #Kick off our tree at the upper left
        return dfs(0,0)        