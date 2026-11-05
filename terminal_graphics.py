
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




def main_terminal(grid):

    left_maze = Maze_terminal(grid)
    right_maze = Maze_terminal(grid)

    terminal_windows = (left_maze, right_maze)

    return terminal_windows

def print_maze_terminal(terminal_windows, maze):

    print(f"       LEFT WALL FOLLOWER                     RIGHT WALL FOLLOWER")
    
    for row in range(len(maze)):
        print(f"{"  ".join(terminal_windows[0].terminal_view[row])}        {"  ".join(terminal_windows[1].terminal_view[row])}")
        
    print("\n \n")


    
def update(terminal_windows, solvers, maze, GOAL):

    for maze_view, solver in zip(terminal_windows, solvers):
        maze_view.solver_marker(solver.position)
        if (solver.position != GOAL):
            direction = solver.movement_direction()
            solver.one_move(direction)

    print_maze_terminal(terminal_windows, maze)
            
       

def final_update(terminal_windows, solvers, maze):

    for window in range(len(terminal_windows)):
        terminal_windows[window].maze()
        terminal_windows[window].solver_marker(solvers[window].position)

    print_maze_terminal(terminal_windows, maze)

    print(f"total steps taken: LEFT = {solvers[0].step_count}   RIGHT = {solvers[1].step_count}")

    