
def champ_asteroides(v, c, n, tailles):
    """
    :param v: Volume de carburant initial
    :type v: int
    :param c: Quantité nécessaire pour éviter un astéroïde de taille 1.
    :type c: int
    :param n: Nombre d'astéroïdes sur le chemin
    :type n: int
    :param tailles: Liste des tailles d'astéroïdes
    :type tailles: list[int]
    """
    carburant = []
    for i in range(len(tailles)):
        quantite = c*tailles[i]
        if tailles[i] <= 20 and quantite > 40:
            carburant.append(40)
        elif tailles[i] >= 80 and quantite > 120:
            carburant.append(120)
        else:
            carburant.append(quantite)
    
    
    rep = 0
    for i in carburant:
        rep += i
    
    if v - rep <= 0:
        return -1
    else:
        return rep
    
if __name__ == '__main__':
    v = int(input())
    c = int(input())
    n = int(input())
    tailles = list(map(int, input().split()))
    print(champ_asteroides(v, c, n, tailles))
