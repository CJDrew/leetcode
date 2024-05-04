heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

visited = set()
def dfs(x, y, lastHeight):
    print(f"{x}, {y}")
    if (x, y) in visited:
        return False
    elif x < 0 or y < 0:
        print('Pacific')
        return True
    elif x >= len(heights[0]) or y >= len(heights):
        print('Atlantic')
        return True
    curHeight = heights[y][x]
    if curHeight > lastHeight:
        return False
    visited.add((x, y))
    pacific = dfs(x-1, y, curHeight) or dfs(x, y-1, curHeight)
    atlantic = dfs(x+1, y, curHeight) or dfs(x, y+1, curHeight)
    visited.remove((x, y))
    if lastHeight == float('inf'):
        print(f"{x}, {y} : {pacific} {atlantic}")
    return pacific and atlantic

print(dfs(1, 3, float('inf')))