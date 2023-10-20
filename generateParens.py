def generateParenthesis(n: int):
        ans = []
        def dfs(cur, l, r):
            if l == 0 and r == 0:
                ans.append(cur)
            if l > 0:
                #try left
                dfs(cur + "(", l-1, r)
            if r > 0 and r > l:
                #try right
                dfs(cur + ")", l, r-1)
        
        dfs("", n, n)
        return ans

generateParenthesis(3)