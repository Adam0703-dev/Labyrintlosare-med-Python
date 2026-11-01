class positionering:


    def __init__(self, position, lista, riktning, antal_steg, version):

        self.riktning = riktning
        self.position = position
        self.lista = lista
        self.antal_steg = antal_steg
        self.version = version

    def rorelse_riktning(self):

        riktning = self.riktning


        if riktning == (1, 0): #riktad ned
            vanster = (0, 1)
            hoger = (0, -1) 
            bak = (-1,0)
            fram = (1,0)
        elif riktning == (0, -1): #riktad vanster
            vanster = (1, 0)
            hoger = (-1, 0) 
            bak = (0,1)
            fram = (0,-1)   
        elif riktning == (0,1): #riktad hoger
            vanster = (-1, 0)
            hoger = (1, 0) 
            bak = (0,-1)
            fram = (0,1) 
        elif riktning == (-1, 0): #riktad upp
            vanster = (0, -1)
            hoger = (0, 1)
            bak = (1, 0)
            fram = (-1, 0)

        vanster_losare = (vanster, fram, hoger, bak)
        hoger_losare = (hoger, fram, vanster, bak)

        return (vanster_losare, hoger_losare)


    def rorelse(self, algoritm):

        lista = self.lista               
        rad, kolumn = self.position

        if self.version == "vanster":
            algoritm = algoritm[0]

        else:
            algoritm = algoritm[1]

        for rotation in algoritm:

            if (len(lista) > (rad + rotation[0]) >= 0) and (len(lista[rad]) > (kolumn + rotation[1])  >= 0) and (lista[rad][kolumn] == 0): 

                if lista[rad + rotation[0]][kolumn + rotation[1]] == 0:
                    rad += rotation[0]
                    kolumn += rotation[1]
                    self.riktning = rotation 
                    self.position = (rad, kolumn)
                    self.antal_steg += 1
                    return None

