def boite_aux_lettres(nom, n, noms):
    """
    :param nom: nom erroné noté sur le colis
    :type nom: str
    :param n: nombre de boîtes aux lettres nom erroné noté sur le colis
    :type n: int
    :param noms: N noms de familles
    :type noms: list[str]
    """
    
    win = [0,""]
    i=0
    while i != len(noms):
        count=0
        if len(nom) == len(noms[i]):
            for y in range(len(nom)):
                if nom[y] == noms[i][y]:
                    count += 1
        
            if win[0] < count :
                win[0] = count
                win[1] = noms[i]
        i += 1
    print(win[1])

if __name__ == '__main__':
    nom = input()
    n = int(input())
    noms = [input() for _ in range(n)]
    boite_aux_lettres(nom, n, noms)