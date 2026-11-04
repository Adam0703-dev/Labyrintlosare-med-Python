class Movement:
    """
    klassen representerar hela lösaren, fran dess aktuella position och riktning till hur många steg den tagit
    """

    def __init__(self, position, maze, direction, step_count, name):
        """"
        Metoden initerar nödvandiga parameterar för klassen
        inparameter: position, maze, direction, step_count, name (tupel, lista, tupel, int, str)
        return: None
        """


        self.direction = direction
        self.position = position
        self.maze = maze
        self.step_count = step_count
        self.name = name



    def movement_direction(self):
        """
        Metoden bestämmer nya värden för fram, bak, höger och vänster utifrån aktuell riktning
        inparameter: None
        return: solvers (tupler av tupler)
        """

        direction = self.direction

        left = (direction[1] * -1, direction[0])
        right = (direction[1], direction[0] * -1)
        back = (direction[0] * -1, direction[1] * -1)
        forward = (direction[0], direction[1])

        left_solver = (left, forward, right, back)
        right_solver = (right, forward, left, back)
        solvers = (left_solver, right_solver)

        return solvers




    def one_move(self, solvers):
        """
        Metoden ansvarar för och uppdaterar vilken riktning och position, samt hur många steg varje lösare har efter varje steg.
        inparameter: solvers (tupler av tupler) - nya och definerade riktningar
        return: None
        """

        maze = self.maze               
        row, column = self.position

        if self.name == "left":
            solver = solvers[0]

        elif self.name == "right":
            solver = solvers[1]

        else:
            return None

        for rotation in solver:

            if (len(maze) > (row + rotation[0]) >= 0) and (len(maze[row]) > (column + rotation[1])  >= 0) and (maze[row][column] == 0): 

                if maze[row + rotation[0]][column + rotation[1]] == 0:
                    row += rotation[0]
                    column += rotation[1]
                    self.direction = rotation 
                    self.position = (row, column)
                    self.step_count += 1
                    return None


