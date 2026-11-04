import graphics
from algorithm import *
import maze_generator




def terminal():

    print(f"""
    Welcome to the Maze solver!
    
    1. Open graphic view
    2. End program
    """)

    choice = input("Choose an alternative (1-2): ")
    return choice

def main():

    file = "maze.txt"
    maze = maze_generator.maze_reader(file)

    START = (0 , 1)
    GOAL = (len(maze) - 1, len(maze[-1]) - 2) #näst sista kolumnen av bottenraden av labyrinten
    step_count = 0  
    position = START
    start_direction = (1, 0) #ned
    left_solver = Movement(position, maze, start_direction, step_count, "left")
    right_solver = Movement(position, maze, start_direction, step_count, "right")
    solutions = (left_solver, right_solver)

    while True:

        choice = terminal()

        if choice == "1":
            maze_frame = graphics.main_window(position, maze, step_count)
            maze_frame[0].after(100, graphics.update, maze_frame, solutions, GOAL) #Ett labyrintfönster väljs for att initera loopen
            maze_frame[0].mainloop()

        elif choice == "2":
            break

        else:
            print(f"Invalid input. Try again.")


if __name__ == "__main__":
     main()
