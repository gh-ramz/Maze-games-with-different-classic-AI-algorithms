from collections import deque

def solve_bfs(maze):

    start = (0, 0)
    end = (maze.shape[0] - 1, maze.shape[1] - 1)

    
    queue = deque([start])
    came_from = {start: None}  

    while queue:
        current = queue.popleft()

        if current == end:
            return  (came_from, current)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
            neighbor = (current[0] + dx, current[1] + dy)

            if (0 <= neighbor[0] < maze.shape[0] and
                0 <= neighbor[1] < maze.shape[1] and
                maze[neighbor[0], neighbor[1]] == 0 and  
                neighbor not in came_from):  
                queue.append(neighbor)
                came_from[neighbor] = current  

    return []  

def reconstruct_path(came_from, current):

    total_path = [current]
    while current in came_from and came_from[current] is not None:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()  
    return total_path


