import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Importing the functions
from aStar import solve_astar
from bfs import solve_bfs
from dfs import solve_dfs
from greedy import solve_greedy

def generate_random_maze(rows, cols):
    """Generates a random maze with more empty cells."""
    return np.random.choice([0, 1], size=(rows, cols), p=[0.7, 0.3])  # More empty cells

def draw_maze(maze, path=None):
    """Draws the maze and optionally highlights a path."""
    plt.clf()  # Clear the current figure
    plt.imshow(maze, cmap='binary', vmin=0, vmax=1)  # 0 for black (empty), 1 for white (blocked)

    # Draw start and end points
    plt.scatter(0, 0, color='red', s=100, label='Start (0,0)')
    plt.scatter(maze.shape[1]-1, maze.shape[0]-1, color='green', s=100, label='End (N-1,N-1)')

    if path is not None:
        # Draw the path in blue
        path_y, path_x = zip(*path)
        plt.plot(path_x, path_y, color='blue', linewidth=3)

    plt.xticks([])
    plt.yticks([])
    plt.title('Random Maze')
    plt.legend()
    plt.draw()

def create_maze():
    """Generates and displays a new maze."""
    global maze
    rows, cols = 20, 20
    maze = generate_random_maze(rows, cols)
    maze[0, 0] = 0  # Start point (must be empty)
    maze[rows-1, cols-1] = 0  # End point (must be empty)
    draw_maze(maze)

def run_astar():
    """Run the A* algorithm and draw the result."""
    path = solve_astar(maze)
    draw_maze(maze, path)

def run_bfs():
    """Run the BFS algorithm and draw the result."""
    path = solve_bfs(maze)
    draw_maze(maze, path)

def run_dfs():
    """Run the DFS algorithm and draw the result."""
    path = solve_dfs(maze)
    draw_maze(maze, path)

def run_greedy():
    """Run the Greedy algorithm and draw the result."""
    path = solve_greedy(maze)
    draw_maze(maze, path)

# Set up the main application window
root = tk.Tk()
root.title("Maze Solver")

# Create a canvas for matplotlib
fig = plt.figure(figsize=(6, 6))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Create buttons
button_frame = tk.Frame(root)
button_frame.pack()

btn_generate = tk.Button(button_frame, text="Generate New Maze", command=create_maze)
btn_generate.grid(row=0, column=0, padx=5, pady=5)

btn_astar = tk.Button(button_frame, text="Solve with A*", command=run_astar)
btn_astar.grid(row=0, column=1, padx=5, pady=5)

btn_bfs = tk.Button(button_frame, text="Solve with BFS", command=run_bfs)
btn_bfs.grid(row=0, column=2, padx=5, pady=5)

btn_dfs = tk.Button(button_frame, text="Solve with DFS", command=run_dfs)
btn_dfs.grid(row=0, column=3, padx=5, pady=5)

btn_greedy = tk.Button(button_frame, text="Solve with Greedy", command=run_greedy)
btn_greedy.grid(row=0, column=4, padx=5, pady=5)

# Start the main loop
create_maze()  # Generate the initial maze
root.mainloop()



