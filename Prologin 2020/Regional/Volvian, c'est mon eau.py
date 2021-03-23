def volvian(p, m):
    """
    :param p: Prix de la commande
    :type p: int
    :param m: Montant payé par le client
    :type m: int
    """
    monnaie = [200,100,50,20,10,5,2,1] 
    if p == m:
        return 0
    rendu = m-p
    nb = 0
    while rendu != 0:
        for i in range(len(monnaie)):
            if (rendu - monnaie[i]) >= 0:
                rendu -= monnaie[i]
                nb += 1
                break
    return nb

if __name__ == '__main__':
    p = int(input())
    m = int(input())
    print(volvian(p, m))
