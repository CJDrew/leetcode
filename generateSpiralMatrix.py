def generateMatrix(n):
        matrix = [[None for j in range(n)] for i in range(n)]

        x, y = 0, 0
        xMin, yMin, xMax, yMax = 0, 1, n-1, n-1
        xDir, yDir = 1, 0

        for i in range(1, (n**2)+1):
            matrix[x][y] = i

            #move x and y to the correct spot
            if xDir == 1 and x == xMax:
                xDir, yDir = 0, 1
                xMax -= 1
            elif yDir == 1 and y == yMax:
                xDir, yDir = -1, 0
                yMax -= 1
            elif xDir == -1 and x == xMin:
                xDir, yDir = 0, -1
                xMin += 1
            elif yDir == -1 and y == yMin:
                xDir, yDir = 1, 0
                yMin += 1
            
            x += xDir
            y += yDir
        
        return matrix

generateMatrix(3)