"""
Main ansvarar för att starta och köra programmet "The Maze Solver" som både via grafiskt användargränssnitt och terminalen
kan generera en labyrint, såväl som låta två lösare, en som följer vänster vägg, och en som följer höger vägg, lösa labyrinten

"""

import graphics
from algorithm import *
import maze_generator
import terminal_graphics
from terminal_graphics import clear_terminal

def terminal():
    """
    funktionen anvarar för att ta skapa användarmenyn för programmet
    inparameter: None
    return: choice (int)
    """

    print(f"""
    Welcome to the Maze solver!
    
    1. Start program in terminal
    2. Generate new maze
    3. Open graphic view
    4. End program
    """)

    choice = input("Choose an alternative (1-4): ")
    return choice


def initiate_terminal_maze(solvers, maze, GOAL):
    """
    funktionen ansvarar för att sätta igång vyn för labyrinterna med dess lösare i terminalen
    inparameter: solvers, maze, GOAL
    

    """

    terminal_windows = terminal_graphics.main_terminal(maze)
    terminal_graphics.update(terminal_windows, solvers, maze, GOAL)
    terminal_graphics.final_update(terminal_windows, solvers, maze)
    


def initiate_random_maze_generator(maze, direction):

    clear_terminal()
    miner_position = (1,1)
    new_maze = maze_generator.create_empty_maze(maze)
    maze_generator.update(new_maze, miner_position, direction)
    return new_maze
    


def initiate_graphic_maze(position, direction, maze, solvers, step_count, GOAL):

    clear_terminal()

    

    # ASSE sa att jag inte ska ha nestlade funktioner, men det behövs då jag skapar create_new_maze_button objektet som 
    #behövs för buttonpress, samtidigt som buttonpress funktionen behövs i create_main_window som behövs för att skapa knappen

    window = graphics.Maze_window(position, direction, maze, step_count, GOAL,
    lambda: initiate_random_maze_generator(maze, direction))
    window.maze_frame[0].after_id = window.maze_frame[0].after(100, graphics.update, window.maze_frame, solvers,
    GOAL, window.create_new_maze_button)
    #Ett labyrintfönster väljs for att initera uppdaterings loopen
    window.maze_frame[0].mainloop()




def main():

    file = "maze.txt"

    try:

        maze = maze_generator.maze_reader(file)


        START = (0 , 1)
        GOAL = (len(maze) - 1, len(maze[-1]) - 2) #näst sista kolumnen av bottenraden av labyrinten
        step_count = 0  
        position = START
        start_direction = (1, 0) #ned

        clear_terminal()

        while True:


            left_solver = Maze_solver(position, maze, start_direction, step_count, "left")
            right_solver = Maze_solver(position, maze, start_direction, step_count, "right")
            solvers = (left_solver, right_solver)

            choice = terminal()

            if choice == "1":
                initiate_terminal_maze(solvers, maze, GOAL)

            elif choice =="2":
                maze = initiate_random_maze_generator(maze, start_direction)
                print("\n    New maze generated")


            elif choice == "3":
                initiate_graphic_maze(position, start_direction, maze, solvers, step_count, GOAL)
                

            elif choice == "4":
                clear_terminal()
                break

            else:
                print(f"\nInvalid input. Try again.")

    except FileNotFoundError:
        clear_terminal()
        print("Maze not found")



if __name__ == "__main__":
     main()
