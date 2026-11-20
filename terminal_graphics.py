"""
Adam Odeh 2026-11-16

Filen terminal_graphics ansvarar för att skapa labyrinten så att den kan ses i terminalen
"""

import time
import os

class Maze_terminal:
    """
    Klassen Maze_terminal ansvarar för att skapa varje vy objekt i terminalen
    """
    
    def __init__(self, grid):
        """
        Konstruktorn används för att ge nödvändiga attribut för varje objekt/metod
        inparameter: grud
        """
        self.grid = grid
        self.maze()



    def maze(self):
        """
        Metoden ansvarar för att skapa labyrinten, från ettor och nollor, till "#" och " " 
        inparameter: None
        return: None
        """

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
        """
        Metoden ansvarar för att omvandla markörens position i labyrinten till "X"
        inparameter: position (tupel)
        return: None
        """

        row, column = position
        self.terminal_view[row][column] = "X"


def clear_terminal():
    """
    Funktionen ansvarar för att rensa terminalen
    inparameter: None
    return: None
    """

    os.system("cls")



def main_terminal(grid):
    """
    Funktionen ansvarar för att skapa terminal vy objekten för varje lösare
    inparameter: grid (matrix)
    return: terminal_windows (tupler av objekt ur klassen Maze_terminal)
    """

    left_maze = Maze_terminal(grid)
    right_maze = Maze_terminal(grid)

    terminal_windows = (left_maze, right_maze)

    return terminal_windows



def print_maze_terminal(terminal_windows, maze):
    """
    Funktionen ansvarar för att skriva utt varje labyrint vy med dess markör bredvid varandra i terminalen.
    inparameter: terminal_windows, maze (tupler av objekt ur klassen Maze_terminal, matrix)
    """

    print(f"       LEFT WALL FOLLOWER                     RIGHT WALL FOLLOWER")
    
    for row in range(len(maze)):
        print(f"{"  ".join(terminal_windows[0].terminal_view[row])}        {"  ".join(terminal_windows[1].terminal_view[row])}")

    

    
def update(terminal_windows, solvers, maze, GOAL):
    """
    Funktionen ansvarar för att uppdatera varje vy efter varje steg, genom att rensa och printa ut en ny
    labyrint för varje steg
    inparameter: terminal_windows, solvers, maze, GOAL (tupler av objekt ur klassen Maze_terminal,
    tupler av objekt ur klassen Maze_solver från modulen "algorithm.py", matrix, tupler) 
    return: None
    """

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
    time.sleep(0.1)
    
        
            


def final_update(terminal_windows, solvers, maze):
    """
    Funktionen ansvarar att printa ut den slutliga vyn för varje lösare och dess labyrint med antalet steg varje lösare tagit
    inparameter: terminal_windows, solvers, maze
    (tupler av objekt ur klassen Maze_terminal, tupler av objekt ur klassen Maze_solver från modulen "algorithm.py", matrix)
    return: None
    """

    clear_terminal()
    for window, solver in zip(terminal_windows, solvers):
        window.maze()
        window.solver_marker(solver.position)

    print_maze_terminal(terminal_windows, maze)

    print(f"\nTotal steps taken: LEFT = {solvers[0].step_count}   RIGHT = {solvers[1].step_count}")