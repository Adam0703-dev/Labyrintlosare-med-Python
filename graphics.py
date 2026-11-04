from tkinter import *

length = 600


class Maze_frame(Frame):
    """
    Denna klass ansvarar för labyrintvyerna
    """

    def __init__(self, position, maze, step_count, name):
        super().__init__()
        self.square_length = (length/(len(maze)))
        self.name = name
        self.position = position
        self.step_count = step_count
        self.maze = maze
        self.frame()
        self.maze_grid(maze)
        self.current_position(position, step_count)

    def frame(self):
        self.label = Label(self)
        self.label.grid(row = 0)
        self.canvas = Canvas(self, width = length, height = length, bg = "black")
        self.canvas.grid(row = 1)


    def current_position(self, position, step_count): 
                name = self.name
                row, column = position
                x = column * self.square_length
                y = row * self.square_length
                end_x = (column + 1) * self.square_length
                end_y = (row + 1) * self.square_length
                self.canvas.coords(self.box, x + self.square_length/10, y + self.square_length/10, end_x - self.square_length/10, end_y - self.square_length/10)
                self.label.config(text = name + " step count =  " + str(step_count), fg = "black", font = 18)

    def maze_grid(self, maze):

        position = self.position

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

        self.box = self.canvas.create_rectangle(position[1] * self.square_length + self.square_length/10, position[0] * self.square_length + self.square_length/10, (position[1] + 1) * self.square_length - self.square_length/10, (position[0] + 1) * self.square_length - self.square_length/10, fill = "white")




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
