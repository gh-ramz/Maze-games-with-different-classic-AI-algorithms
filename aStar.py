import numpy as np
from queue import PriorityQueue

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solve_astar(maze):
    start = (0, 0)
    end = (maze.shape[0] - 1, maze.shape[1] - 1)
    
    
    open_set = PriorityQueue()
    open_set.put((0, start))
    
    came_from = {} 
    g_score = {start: 0} 
    f_score = {start: heuristic(start, end)}  

    while not open_set.empty():
        current = open_set.get()[1]

        if current == end:
            return reconstruct_path(came_from, current)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  
            neighbor = (current[0] + dx, current[1] + dy)

            
            if 0 <= neighbor[0] < maze.shape[0] and 0 <= neighbor[1] < maze.shape[1]:
                if maze[neighbor[0], neighbor[1]] == 1:  
                    continue  

                
                tentative_g_score = g_score[current] + 1  

                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    open_set.put((f_score[neighbor], neighbor))

    return []  

def reconstruct_path(came_from, current):
    
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()  
    return total_path