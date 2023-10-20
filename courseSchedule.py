def canFinish(numCourses, prerequisites):
    #Detect a loop in the prereqs list = not possible

    #Fill out list of prereqs so that each key represents a class and the list represents all of
    #its prereqs
    reqs = {}
    for i in range(numCourses):
        reqs[i] = []
    for req in prerequisites:
        reqs[req[0]].append(req[1])

    def dfs(root, visited):
        if root in visited:
            return False
        if len(reqs[root]) == 0:
            return True
        for p in reqs[root]:
            if not dfs(p, visited + [root]):
                return False
        reqs[root] = []
        return True
    
    #For each class follow the tree and see if there's a loop
    for c in reqs.keys():
        if not dfs(c, []):
            return False
    
    return True

print(canFinish(8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]))