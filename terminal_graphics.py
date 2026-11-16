import time
import os
class Maze_terminal():


    def __init__(self, grid):
        self.grid = grid
        self.maze()



    def maze(self):

        grid = self.grid

        self.terminal_view = []
        
        for row in range(len(grid)):
            new_row = []
            for column in range(len(grid[row])):
                if grid[row][column] == 1:
                    new_row.append("#")
                elif grid[row][column] == 0:
                    new_row.append(" ")
            self.terminal_view.append(new_row)


    def solver_marker(self, position):

        row, column = position
        self.terminal_view[row][column] = "X"


def clear_terminal():

    os.system("cls")

def main_terminal(grid):

    left_maze = Maze_terminal(grid)
    right_maze = Maze_terminal(grid)

    terminal_windows = (left_maze, right_maze)

    return terminal_windows



def print_maze_terminal(terminal_windows, maze):

    print(f"       LEFT WALL FOLLOWER                     RIGHT WALL FOLLOWER")
    
    for row in range(len(maze)):
        print(f"{"  ".join(terminal_windows[0].terminal_view[row])}        {"  ".join(terminal_windows[1].terminal_view[row])}")

    

    
def update(terminal_windows, solvers, maze, GOAL):

    while (solvers[0].position != GOAL) or (solvers[1].position != GOAL):
        for maze_view, solver in zip(terminal_windows, solvers):
            maze_view.solver_marker(solver.position)
            if solver.position != GOAL:
                direction = solver.movement_direction()
                solver.one_move(direction)
            time.sleep(0.1)

        clear_terminal()
        print_maze_terminal(terminal_windows, maze)
        terminal_windows = main_terminal(maze)
    time.sleep(0.2)
    
        
            


def final_update(terminal_windows, solvers, maze):

    clear_terminal()
    for window, solver in zip(terminal_windows, solvers):
        window.maze()
        window.solver_marker(solver.position)

    print_maze_terminal(terminal_windows, maze)

    print(f"\nTotal steps taken: LEFT = {solvers[0].step_count}   RIGHT = {solvers[1].step_count}")
