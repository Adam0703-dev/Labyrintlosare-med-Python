"""
Adam Odeh 2026-11-16

filen maze_generator läser in en labyrint från en textfil - maze.txt - och omvandlar texten till ett grid som programmet
kan läsa från, ettor och nollor. Maze_generator ansvarar också för att skapa nya labyrinter med olika strukturer

källor:
https://docs.python.org/3/library/random.html  Shuffle.
"""

import random

def maze_reader(file):
    """
    Funktionen ansvarar för att läsa in värdena ur en textfil och omvandla den till en matris av integers
    inparameter: file (str)
    return: maze (matrix)
    """


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
    """
    Funktionen ansvarar för att skapa en matris av enbart ettor - labyrint fylld av väggar
    inparameter: maze (matrix)
    return: new_maze (matrix)
    """

    new_maze = []

    side_length = len(maze)

    for _ in range(side_length):
        row_list = []
        for _ in range(side_length):
            row_list.append(1)
        new_maze.append(row_list)
    new_maze[0][1] = 0 #Start
    new_maze[-1][-2] = 0 #Mål

    return new_maze



def miner(new_maze, position, direction, stack):
    """
    Funtionen ansvarar för varje ett steg i skapandet av gången (från ett till noll) för den slumpade labyrinten 
    via en depth first search algoritm
    inparameter: new_maze, position, direction, stack (matrix, tupel, tupel, list)
    return: new_maze, position, direction, stack (matrix, tupel, tupel, list)
    """

    directions = [(1,0), (0,-1), (-1,0), (0,1)] #ned, vänster, upp, höger

    random.shuffle(directions)


    for direction in directions:
        

        if (((len(new_maze) - 1) > (position[0] + 2 * direction[0]) > 0)
        and (len(new_maze[0]) - 1) > (position[1] + 2 * direction[1])  > 0):

            if new_maze[position[0]][position[1]] == 1:
                new_maze[position[0]][position[1]] = 0
            
            if new_maze[position[0] + 2 * direction[0]][position[1] + 2 * direction[1]] == 1:
                position = (position[0] + 2 * direction[0], position[1] + 2 * direction[1])
                new_maze[position[0]][position[1]] = 0
                new_maze[position[0] - direction[0]][position[1] - direction[1]] = 0
                stack.append(position)
                break

    else:
            stack.pop()
            if stack != []:
                position = stack[-1]

    if len(new_maze) % 2 == 0:
        new_maze[- 2][-2] = 0
        new_maze[-3][-2] = 0
             
            
    return new_maze, position, direction, stack



def update(new_maze, position, direction):
    """
    Funktionen ansvarar för uppdatingen av funktionen miner, så att en fullständig labyrint från start till slut skapas.
    inparameter: new_maze, position, direction (matrix, tupel, tupel)
    return: new_maze, position, direction (matrix, tupel, tupel)
    """

    stack = [position]

    while stack != []:
        
        new_maze, position, direction, stack = miner(new_maze, position, direction, stack)

    return new_maze, position, direction, stack
        