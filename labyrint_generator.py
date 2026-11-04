

def las_in_labyrint(fil):

    lista = []
    with open(fil, "r", encoding="utf-8") as fil:
        layout = fil.readline().strip()
        while layout != "":
            layout = layout.split(",")
            for nummer in range(len(layout)):
                for varde in layout[nummer]:
                    varde = int(varde)
                    layout[nummer] = varde
            lista.append(layout)
            layout = fil.readline().strip()

        return lista



"""
Använd stack för backtracking och kolla alltid två steg framåt, gå två steg bak OSV. då en vägg är en hel ruta.
 Använd dig av randomized depth-first search - iterative implementation

Du behöver inleda varje program med att sätta hela txt filen till ettor förutom start och noll, sedan låta programmet
köra en rad in. det blir (rad + 1, kolumn + 1)  till (len(rad) + 2), len(kolumn) + 2)
"""
            