def solve_greedy(maze):
    
    start = (0, 0)
    end = (maze.shape[0] - 1, maze.shape[1] - 1)

    if maze[start[0], start[1]] != 0 or maze[end[0], end[1]] != 0:
        return []  

    path = [start]
    current = start
    visited = set() 
    visited.add(current)

    while current != end:
    
        neighbors = []
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if (0 <= neighbor[0] < maze.shape[0] and
                0 <= neighbor[1] < maze.shape[1] and
                maze[neighbor[0], neighbor[1]] == 0 and 
                neighbor not in visited):  
                neighbors.append(neighbor)

        if not neighbors:  
            return [] 

        
        current = min(neighbors, key=lambda n: (n[0] - end[0]) ** 2 + (n[1] - end[1]) ** 2)
        path.append(current)
        visited.add(current)  
    return path
