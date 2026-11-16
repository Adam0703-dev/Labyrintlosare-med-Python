import graphics
from algorithm import *
import maze_generator
import terminal_graphics
from terminal_graphics import clear_terminal

def terminal():

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

    def buttonpress():
        new_maze = initiate_random_maze_generator(maze, direction)
        graphics.generate_new_maze(new_maze, maze_frame, position, direction, step_count, create_new_maze_button,
        GOAL)


    maze_frame, create_new_maze_button = graphics.create_main_window(position, maze, step_count, buttonpress)
    maze_frame[0].after_id = maze_frame[0].after(100, graphics.update, maze_frame, solvers, GOAL, create_new_maze_button)
    #Ett labyrintfönster väljs for att initera uppdaterings loopen
    maze_frame[0].mainloop()




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
