"""


källor:
https://docs.python.org/3/library/random.html  Shuffle.
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

    new_maze = []
    
    for _ in range(len(maze)):
        row_list = []
        for _ in range(len(maze)):
            row_list.append(1)
        new_maze.append(row_list)
    new_maze[0][1] = 0 #Start
    new_maze[len(maze)-1][len(maze[-1])-2] = 0 #Mål
    return new_maze



def miner(new_maze, position, direction, stack):

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
             
            
    return new_maze, position, direction, stack



def update(new_maze, position, direction):

    stack = [position]

    while stack != []:
        
        new_maze, position, direction, stack = miner(new_maze, position, direction, stack)

    return new_maze, position, direction, stack
        

        


    


"""
Använd stack för backtracking och kolla alltid två steg framåt, gå två steg bak OSV. då en vägg är en hel ruta.
Använd dig av randomized depth-first search - iterative implementation

Du behöver inleda varje program med att sätta hela txt filen till ettor förutom start och noll, sedan låta programmet
köra en rad in. det blir (rad + 1, kolumn + 1)  till (len(rad) + 2), len(kolumn) + 2)
"""
            