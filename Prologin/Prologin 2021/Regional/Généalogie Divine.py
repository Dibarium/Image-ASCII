def genealogie_divine(f, m, familles, c, cartes):
    """
    :param f: Le nombre de familles
    :type f: int
    :param m: Le nombre de membres par famille
    :type m: int
    :param familles: Les différentes familles possibles dans le jeu
    :type familles: list[list[str]]
    :param c: Le nombre de cartes dans la main de Joseph
    :type c: int
    :param cartes: Les cartes dans la main de Joseph
    :type cartes: list[str]
    """
    liste = []
    valeur = [0 for i in range(len(familles))]
    for i in range(len(cartes)):
        liste.append(cartes[i])
    for i in range(len(familles)):
        for y in range(len(familles[i])):
            if familles[i][y] in liste:
                valeur[i]+=1
    return -(max(valeur)-m)


if __name__ == '__main__':
    f = int(input())
    m = int(input())
    familles = [list(input()) for _ in range(f)]
    c = int(input())
    cartes = list(input())
    print(genealogie_divine(f, m, familles, c, cartes))
