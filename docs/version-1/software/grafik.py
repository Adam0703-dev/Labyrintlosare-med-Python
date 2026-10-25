from tkinter import *




class Labyrintfonster(Tk):

    def __init__(self, position, lista):
        super().__init__()
        self.canvas = Canvas(width = 600, height = 600, bg = "black", bd = 2, relief = "flat", highlightthickness = 0)
        self.canvas.pack()
        self.position = position 
        self.lista = lista
        self.bana(lista)
        self.box = self.canvas.create_rectangle(position[1] * 100 + 10, position[0] * 100 + 10, (position[1] + 1) * 100 - 10, (position[0] + 1) * 100 - 10, fill = "white")
        self.ny_position(position)


    def ny_position(self, position):                                                
                rad, kolumn = position
                x = kolumn * 100
                y = rad * 100
                slut_x = (kolumn + 1) * 100
                slut_y = (rad + 1) * 100
                self.canvas.coords(self.box, x + 10, y + 10, slut_x - 10, slut_y - 10)

    def bana(self, lista):
        
        for rad in range(len(lista)):
            for kolumn in range(len(lista[rad])):
                if lista[rad][kolumn] == 0:
                    x = kolumn * 100
                    y = rad * 100
                    slut_x = (kolumn + 1) * 100
                    slut_y = (rad + 1) * 100
                    self.canvas.create_rectangle(x, y, slut_x, slut_y, fill = "black", width = 5)
                else:
                    x = kolumn * 100
                    y = rad * 100
                    slut_x = (kolumn + 1) * 100
                    slut_y = (rad + 1) * 100
                    self.canvas.create_rectangle(x, y, slut_x, slut_y, fill = "green", width = 5)








