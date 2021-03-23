def parcour(ligne, colonne, panel, nb):
    print([ligne],[colonne])
    
    if panel[ligne][colonne] == "C":
        nb += 1
    panel[ligne][colonne] = "."
    if colonne - 1 >= 0:
        if panel[ligne][colonne - 1] != ".":
            if panel[ligne][colonne - 1] == "C":
                nb += 1
                panel[ligne][colonne - 1] = "."
            elif panel[ligne][colonne - 1] == "+" :
                nb = parcour(ligne, colonne-1, panel, nb)
            
    if colonne + 1 <= len(panel[ligne])-1:
        if panel[ligne][colonne + 1] != ".":
            if panel[ligne][colonne + 1] == "C":
                nb += 1
                panel[ligne][colonne + 1] = "."
            elif panel[ligne][colonne + 1] == "+" : 
                nb = parcour(ligne, colonne + 1, panel, nb)
    if ligne - 1 >= 0:
        if panel[ligne - 1][colonne] != ".":
            if panel[ligne - 1][colonne] == "C":
                nb += 1
                panel[ligne - 1][colonne] = "."
            elif panel[ligne - 1][colonne] == "+" : 
                nb = parcour(ligne - 1, colonne, panel, nb)
    if ligne + 1 <= 4:
        if panel[ligne + 1][colonne] != ".":
            if panel[ligne + 1][colonne] == "C":
                nb += 1
                panel[ligne + 1][colonne] = "."
            if panel[ligne + 1][colonne] == "+" : 
                nb =parcour(ligne + 1, colonne, panel, nb)
    return nb

def charge_me_up(n, panel):
    """
    :param n: Dimensions du panneau de contrôle
    :type n: int
    :param panel: Panneau de contrôle
    :type panel: list[list[str]]
    """
    best = 0
    nb = 0
    ban = []
    for i in range(len(panel)):
        for y in range(len(panel[i])):
            if panel[i][y] == "P":
                nb = parcour(i,y,panel,nb)
                print(nb)
                if nb > best:
                    best = nb
                nb = 0
                    
                    
    return best*6

if __name__ == '__main__':
    n = int(input())
    carte = [list(input()) for _ in range(n)]
    print(charge_me_up(n, carte))
