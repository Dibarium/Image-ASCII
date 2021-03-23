def factorielle(n):
    if n == 0:
        return 1
    else:
        F = 1
        for k in range(2,n+1):
            F = F * k
        return F
def ppcm(a,b):
    p=a*b
    while(a!=b):
        if (a<b): b-=a
        else: a-=b
    return p/a
def trouver_somme(n):
    """
    :param n: dimension du labyrinthe de Minos
    :type n: int
    """
    # TODO Retourne le nombre de chemins possibles dans le labyrinthe de Minos
    # et la somme.
    somme1 = 0
    somme = []
    b=n-1
    a=factorielle(b+b)/(factorielle(b)*factorielle(b))
    a=a/n
    for i in range(1, int(a+1)) :
        for j in range(1, int(a+1)) :
            somme.append(ppcm(i,j))
    for v in somme :
        somme1 = somme1 + v
    print(int(a))
    print(int(somme1))
    pass


if __name__ == '__main__':
    n = int(input())
    trouver_somme(n)