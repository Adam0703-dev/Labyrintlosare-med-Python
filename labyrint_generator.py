

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
            
            
