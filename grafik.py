from tkinter import *

sidlangd = 600


class Labyrintfonster(Frame):
    """
    Denna klass ansvarar för labyrintvyerna
    """

    def __init__(self, position, lista, antal_steg, namn):
        super().__init__()
        self.box_langd = (sidlangd/(len(lista)))
        self.namn = namn
        self.position = position
        self.antal_steg = antal_steg
        self.lista = lista
        self.fonster()
        self.labyrint_monster(lista)
        self.aktuell_position(position, antal_steg)

    def fonster(self):
        self.label = Label(self)
        self.label.grid(row = 0)
        self.canvas = Canvas(self, width = sidlangd, height = sidlangd, bg = "black")
        self.canvas.grid(row = 1)


    def aktuell_position(self, position, antal_steg): 
                namn = self.namn                                               
                rad, kolumn = position
                x = kolumn * self.box_langd
                y = rad * self.box_langd
                slut_x = (kolumn + 1) * self.box_langd
                slut_y = (rad + 1) * self.box_langd
                self.canvas.coords(self.box, x + self.box_langd/10, y + self.box_langd/10, slut_x - self.box_langd/10, slut_y - self.box_langd/10)
                self.label.config(text = namn + " Antal steg =  " + str(antal_steg), fg = "black", font = 18)

    def labyrint_monster(self, lista):

        position = self.position
        box_langd = self.box_langd

        for rad in range(len(lista)):
            for kolumn in range(len(lista[rad])):
                x = kolumn * self.box_langd
                y = rad * self.box_langd
                slut_x = (kolumn + 1) * self.box_langd
                slut_y = (rad + 1) * self.box_langd

                if lista[rad][kolumn] == 0:
                    self.canvas.create_rectangle(x, y, slut_x, slut_y, fill = "black")

                else:
                    self.canvas.create_rectangle(x, y, slut_x, slut_y, fill = "green")

        self.box = self.canvas.create_rectangle(position[1] * box_langd + box_langd/10, position[0] * box_langd + box_langd/10, (position[1] + 1) * box_langd - box_langd/10, (position[0] + 1) * box_langd - box_langd/10, fill = "white")




def huvud_fonster(position, labyrint, antal_steg):
    huvud_fonster = Tk()
    huvud_fonster.geometry("1200x700")
    huvud_fonster.config(bg="black")
    vanster_maze = Labyrintfonster(position, labyrint, antal_steg, "VANSTER:")
    vanster_maze.grid(row = 0, column = 0)
    hoger_maze = Labyrintfonster(position, labyrint, antal_steg, "HOGER:")
    hoger_maze.grid(row = 0, column = 1)

    return (vanster_maze, hoger_maze)
