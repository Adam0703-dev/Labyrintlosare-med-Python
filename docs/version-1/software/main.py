import grafik


labyrint = [[1,0,1,1,1,1],
            [1,0,0,0,1,1],
            [1,0,1,0,1,1],
            [1,0,1,1,1,1],
            [1,0,0,0,0,1],
            [1,1,1,1,0,1]]



START = (0,1)
MOL = (5,4)
position = START

def rorelse(position, lista, riktning):

    rad = position[0]
    kolumn = position[1]
    hoger = (0,1)
    vanster = (0, -1)
    fram = (1, 0)
    bak = (-1, 0)
  
    if rad >= 0 and kolumn >= 0 and lista[rad][kolumn] == 0:


        if riktning == fram:
            vanster = (0, 1)
            hoger = (0, -1) 
            bak = (-1,0)
            fram = (1,0)
        elif riktning == vanster:
            vanster = (1, 0)
            hoger = (-1, 0) 
            bak = (0,1)
            fram = (0,-1)   
        elif riktning == hoger:
            vanster = (-1, 0)
            hoger = (1, 0) 
            bak = (0,-1)
            fram = (0,1) 
        elif riktning == bak:
             vanster = (0, -1)
             hoger = (0, 1)
             bak = (1, 0)
             fram = (-1, 0)

        if lista[rad + vanster[0]][kolumn + vanster[1]] == 0:
             rad += vanster[0]
             kolumn += vanster[1]
             riktning = vanster
             position = (rad, kolumn)
             return position, riktning
        elif lista[rad + fram[0]][kolumn + fram[1]] == 0:
             rad += fram[0]
             kolumn += fram[1]
             riktning = fram
             position = (rad, kolumn)
             return position, riktning
        elif lista[rad + hoger[0]][kolumn + hoger[1]] == 0:
             rad += hoger[0]
             kolumn += hoger[1]
             riktning = hoger
             position = (rad, kolumn)
             return position, riktning
        elif lista[rad + bak[0]][kolumn + bak[1]] == 0:
             rad += bak[0]
             kolumn += bak[1]
             riktning = bak
             position = (rad, kolumn)
             return position, riktning





        
def uppdatera(maze, position, lista, riktning):
        if position != MOL:  
            ny_position = rorelse(position, lista, riktning)
            position, riktning = ny_position
            maze.ny_position(position)
            maze.after(1000, uppdatera, maze, position, lista, riktning)



def main():
    riktning =(1, 0)
    lista = labyrint
    position = START
    maze = grafik.Labyrintfonster(position, lista)
    maze.after(1000, uppdatera, maze, position, lista, riktning)
    maze.mainloop()

main()
