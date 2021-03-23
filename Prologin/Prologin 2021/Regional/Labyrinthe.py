def labyrinthe_demoniaque(a, n, m, plateau):
    """
    :param a: ame du visiteur
    :type a: int
    :param n: longueur du labyrinthe
    :type n: int
    :param m: largeur du labyrinthe
    :type m: int
    :param plateau: grille du labyrinthe
    :type plateau: list[list[int]]
    """
    tableau = []
    coord = []
    save = []
    x=0
    for i in range(len(plateau)):
        if x < 12 and x != 0:
            tableau.append
            save.append(x)
        x = 0
        for y in range(len(plateau[i])):
            x += plateau[y][i]
            tableau.append(y)
        print(x)   
                


if __name__ == '__main__':
    a = int(input())
    n = int(input())
    m = int(input())
    plateau = [list(map(int, input().split())) for _ in range(n)]
    labyrinthe_demoniaque(a, n, m, plateau)
