"""

"""


import random

def maze_reader(file):

    maze = []
    with open(file, "r", encoding="utf-8") as file:
        grid = file.readline().strip()
        while grid != "":
            grid = grid.split(",")
            for cell in range(len(grid)):
                for value in grid[cell]:
                    value = int(value)
                    grid[cell] = value
            maze.append(grid)
            grid = file.readline().strip()

        return maze



def create_empty_maze(maze):
    length = len(maze) - 2
    new_maze = []
    
    for _ in range(length):
        row_list = []
        for _ in range(length):
            row_list.append(1)
        new_maze.append(row_list)
    return new_maze




def miner(position, new_maze, direction, SLUT):

    stack = []      

    if (new_maze[position[0] + direction[0]][position[1] + direction[1]] == SLUT
    or new_maze[position[0] + 2 * direction[0]][position[1] + 2 * direction[1]] == SLUT): 
        if new_maze[position[0]][position[1]] == 1:
            new_maze[position[0]][position[1]] = 0
            stack.append(position)
        else:
            pass
    return new_maze





"""
Använd stack för backtracking och kolla alltid två steg framåt, gå två steg bak OSV. då en vägg är en hel ruta.
Använd dig av randomized depth-first search - iterative implementation

Du behöver inleda varje program med att sätta hela txt filen till ettor förutom start och noll, sedan låta programmet
köra en rad in. det blir (rad + 1, kolumn + 1)  till (len(rad) + 2), len(kolumn) + 2)
"""
            