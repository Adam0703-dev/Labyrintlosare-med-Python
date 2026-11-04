from tkinter import *

length = 600


class Maze_frame(Frame):
    """
    Denna klass ansvarar för labyrintvyerna
    """

    def __init__(self, position, maze, step_count, strategy):
        super().__init__()
        self.square_length = (length/(len(maze)))
        self.strategy = strategy
        self.position = position
        self.step_count = step_count
        self.maze = maze
        self.frame()
        self.maze_grid(maze)
        self.create_solver_marker()

    def frame(self):

        self.label = Label(self)
        self.label.grid(row = 0)
        self.canvas = Canvas(self, width = length, height = length, bg = "black")
        self.canvas.grid(row = 1)



    def step_counter(self, step_count):

        strategy = self.strategy
        self.label.config(text = strategy + " step count =  " + str(step_count), fg = "black", font = 18)


    def create_solver_marker(self):

        position = self.position
        self.box = self.canvas.create_rectangle(position[1] * self.square_length + self.square_length/10, position[0] * self.square_length + self.square_length/10, (position[1] + 1) * self.square_length - self.square_length/10, (position[0] + 1) * self.square_length - self.square_length/10, fill = "white")



    def move_solver_marker(self, position): 
        
                row, column = position
                x = column * self.square_length
                y = row * self.square_length
                end_x = (column + 1) * self.square_length
                end_y = (row + 1) * self.square_length
                self.canvas.coords(self.box, x + self.square_length/10, y + self.square_length/10, end_x - self.square_length/10, end_y - self.square_length/10)

    def maze_grid(self, maze):

        for row in range(len(maze)):
            for column in range(len(maze[row])):
                x = column * self.square_length
                y = row * self.square_length
                end_x = (column + 1) * self.square_length
                end_y = (row + 1) * self.square_length

                if maze[row][column] == 0:
                    self.canvas.create_rectangle(x, y, end_x, end_y, fill = "black")

                else:
                    self.canvas.create_rectangle(x, y, end_x, end_y, fill = "green")




def main_window(position, maze, step_count):

    main_window = Tk()
    main_window.geometry("1200x700")
    main_window.config(bg="black")

    left_maze = Maze_frame(position, maze, step_count, "LEFT:")
    left_maze.grid(row = 0, column = 0)

    right_maze = Maze_frame(position, maze, step_count, "RIGHT:")
    right_maze.grid(row = 0, column = 1)

    window = (left_maze, right_maze)

    return window


def update(maze_frame, solvers, GOAL):

    for maze_view, solver in zip(maze_frame, solvers):
        if solver.position != GOAL:
            direction = solver.movement_direction()
            solver.one_move(direction)
            maze_view.move_solver_marker(solver.position)
            maze_view.step_counter(solver.step_count)

        print(solver.step_count)

    if (solvers[0].position != GOAL) or (solvers[1].position != GOAL):
        maze_view.after(100, update, maze_frame, solvers, GOAL)