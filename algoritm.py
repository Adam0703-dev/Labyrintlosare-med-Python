class positionering:
    """
    klassen representerar hela losaren, fran dess aktuella position och riktning till hur manga steg den tagit
    """

    def __init__(self, position, lista, riktning, antal_steg, version):
        """"
        Metoden initerar nodvandiga varden for klassen
        inparameter: position, lista, riktning, antal_steg, version (tupel, lista, tupel, int, str)
        return: None
        """


        self.riktning = riktning
        self.position = position
        self.lista = lista
        self.antal_steg = antal_steg
        self.version = version

    def rorelse_riktning(self):
        """
        Metoden bestammer nya varden for fram, bak, hoger och vanster utifran aktuell riktning
        inparameter: None
        return: algoritm (tupler av tupler)
        """

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

        return (vanster_losare, hoger_losare) #algoritmerna


    def rorelse(self, algoritm):
        """
        Metoden ansvarar for och uppdaterar vilken riktning och position, samt hur manga steg varje losare har efter varje steg.
        inparameter: algoritm (tupler av tupler) - nya och definerade riktningar
        return: None
        """

        lista = self.lista               
        rad, kolumn = self.position

        if self.version == "vanster":
            algoritm = algoritm[0]

        elif self.version == "hoger":
            algoritm = algoritm[1]

        else:
            return None

        for rotation in algoritm:

            if (len(lista) > (rad + rotation[0]) >= 0) and (len(lista[rad]) > (kolumn + rotation[1])  >= 0) and (lista[rad][kolumn] == 0): 

                if lista[rad + rotation[0]][kolumn + rotation[1]] == 0:
                    rad += rotation[0]
                    kolumn += rotation[1]
                    self.riktning = rotation 
                    self.position = (rad, kolumn)
                    self.antal_steg += 1
                    return None


