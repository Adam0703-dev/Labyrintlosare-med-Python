import grafik
from algoritm import *
import labyrint_generator



        
def uppdatera(maze, losningar, MOL):

    for losare in zip(maze, losningar):
        if losare[1].position != MOL:
            algoritm = losare[1].rorelse_riktning()
            losare[1].rorelse(algoritm)
            losare[0].aktuell_position(losare[1].position, losare[1].antal_steg)

        
    
    losare[0].after(100, uppdatera, maze, losningar, MOL,)

def terminal():

    print(f"""
    Valkommen till labyrintlosaren!
    
    1. Starta Labyrintlosare
    2. Avsluta program
    """)

    val = input("Valj ett alternativ: ")
    return val

def main():

    fil = "labyrint.txt"
    labyrint = labyrint_generator.las_in_labyrint(fil)

    START = (0 , 1)
    MOL = (len(labyrint) - 1, len(labyrint[-1]) - 2) #nast sista kolumnen av bottenraden av labyrinten
    antal_steg = 0  

    position = START
    riktning = (1, 0) #ned
    vanster_losare = positionering(position, labyrint, riktning, antal_steg, "vanster")
    hoger_losare = positionering(position, labyrint, riktning, antal_steg, "hoger")
    losningar = (vanster_losare, hoger_losare)

    while True:

        val = terminal()

        if val == "1":
            maze = grafik.huvud_fonster(position, labyrint, antal_steg)
            maze[0].after(100, uppdatera, maze, losningar, MOL) #En maze valjs for att initera loopen
            maze[0].mainloop()

        elif val == "2":
            break

        else:
            print(f"Alternativet du angav finns inte")


if __name__ == "__main__":
     main()
