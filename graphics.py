"""
Adam Odeh 2026-11-16

filen graphics ansvarar för att skapa det grafiska användargränssnittet för labyrinten.

källor:
https://docs.python.org/3/library/tkinter.html#tkinter.Frame - för grfiska användargränssnittet
https://stackoverflow.com/questions/26168967/invalid-command-name-while-executing-after-script - för exempel 
på hur man löser en bugg med stängningen av ett fönster under körandet


"""


from tkinter import *
from algorithm import *

LENGTH = 600


class Maze_frame(Frame):
    """
    Denna klass ansvarar för labyrintvyerna
    """

    def __init__(self, position, maze, step_count, strategy, after_id):
        super().__init__()
        self.square_length = (LENGTH/(len(maze)))
        self.strategy = strategy
        self.position = position
        self.step_count = step_count
        self.maze = maze
        self.after_id = after_id
        self.frame()
        self.maze_grid(maze)
        self.create_solver_marker()




    def frame(self):

        self.label = Label(self)
        self.label.grid(row = 0)
        self.canvas = Canvas(self, width = LENGTH, height = LENGTH, bg = "black")
        self.canvas.grid(row = 1)



    def step_counter(self, step_count):

        strategy = self.strategy
        self.label.config(text = strategy + " step count =  " + str(step_count), fg = "black", font = 18)


    def create_solver_marker(self):

        position = self.position
        self.box = self.canvas.create_rectangle(
        position[1] * self.square_length + self.square_length/10,
        position[0] * self.square_length + self.square_length/10,
        (position[1] + 1) * self.square_length - self.square_length/10,
        (position[0] + 1) * self.square_length - self.square_length/10, fill = "white")



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



class Maze_window():


    def __init__(self, position, direction, maze, step_count, GOAL, new_maze_function):

        self.create_main_window()

        self.new_maze_function = new_maze_function

        self.generate_maze_frames(position, maze, step_count)
        self.generate_maze_button(lambda: self.buttonpress(position, direction, step_count, GOAL))
        
        self.main_window.protocol("WM_DELETE_WINDOW", self.closed_main_window)   



    def create_main_window(self):

        self.main_window = Tk()
        self.main_window.geometry("1200x700")
        self.main_window.config(bg="black")



    def generate_maze_frames(self, position, maze, step_count):
        
        left_maze = Maze_frame(position, maze, step_count, "LEFT:", 0)
        left_maze.grid(row = 0, column = 0)

        right_maze = Maze_frame(position, maze, step_count, "RIGHT:", 0)
        right_maze.grid(row = 0, column = 1)

        self.maze_frame = (left_maze, right_maze)



    def generate_maze_button(self, buttonpress):

        self.create_new_maze_button = Button(text = "Create new maze", font = 24,
        command = buttonpress, state = "disabled")
        
        self.create_new_maze_button.grid(row=1, columnspan=2)



    def buttonpress(self, position, direction, step_count, GOAL):

        self.new_maze = self.new_maze_function()
        self.restart_maze(position, step_count)
        self.restart_solvers(position, direction, step_count)
        self.maze_frame[0].after_id = self.maze_frame[0].after(100, update, self.maze_frame,
        self.solvers, GOAL, self.create_new_maze_button)



    def closed_main_window(self):

        for frame in self.maze_frame:
            frame.after_cancel(frame.after_id)

        self.main_window.destroy()



    def restart_maze(self, position, step_count):

        self.create_new_maze_button.config(state = "disabled")

        for frame in self.maze_frame:

            frame.canvas.delete("all")
            frame.maze_grid(self.new_maze)
            frame.create_solver_marker()
            frame.step_counter(step_count)
            frame.move_solver_marker(position)


    def restart_solvers(self, position, direction, step_count):

        left_solver = Maze_solver(position, self.new_maze, direction, step_count, "left")
        right_solver = Maze_solver(position, self.new_maze, direction, step_count, "right")
        self.solvers = (left_solver, right_solver)



def update(maze_frame, solvers, GOAL, create_new_maze_button):

    for maze_view, solver in zip(maze_frame, solvers):      #zip - https://docs.python.org/3.3/library/functions.html
        if solver.position != GOAL:
            direction = solver.movement_direction()
            solver.one_move(direction)
            maze_view.move_solver_marker(solver.position)
            maze_view.step_counter(solver.step_count)

    if (solvers[0].position != GOAL) or (solvers[1].position != GOAL):
        maze_view.after_id = maze_view.after(100, update, maze_frame, solvers, GOAL, create_new_maze_button)

    else:
        
        create_new_maze_button.config(state = "normal")