def findOrder(numCourses: int, prerequisites):
    #Fill out adjacency dictionary
    #Key is a class, value is list of prereqs for the class
    dic = {}
    for i in range(numCourses):
        dic[i] = []
    for req in prerequisites:
        dic[req[0]].append(req[1])
    
    #Topological sort method
    stack = []
    foundCycle = False
    #I actually want 3 states: Unvisited: 0, Visiting: 1, Visited: 2
    visited = [0 for i in range(numCourses)]
    def topSort(course):
        #We are looking at the descendents of this course
        visited[course] = 1
        for req in dic[course]:
            #We want to visit something already in the current path. A cycle!
            if visited[req] == 1:
                foundCycle = True
            elif visited[req] == 0:
                topSort(req)
        #We are done witht his course and its descendents
        visited[course] = 2
        stack.append(course)
    
    #Call topological sort for each class
    for course in range(numCourses):
        #Only do unvisited courses to avoid dupes
        if visited[course] == 0:
            topSort(course)

    return stack if not foundCycle else []

print(findOrder(2, [[0,1],[1,0]]))