

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



"""
Använd stack för backtracking och kolla alltid två steg framåt, gå två steg bak OSV. då en vägg är en hel ruta.
 Använd dig av randomized depth-first search - iterative implementation

Du behöver inleda varje program med att sätta hela txt filen till ettor förutom start och noll, sedan låta programmet
köra en rad in. det blir (rad + 1, kolumn + 1)  till (len(rad) + 2), len(kolumn) + 2)
"""
            