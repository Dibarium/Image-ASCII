
def cafe_asteroide(emplacement, etage, carte):
    """
    :param h: hauteur de la carte (longueur)
    :type h: int
    :param l: largeur de la carte
    :type l: int
    :param p: position du vaisseau sur la première ligne de la carte
    :type p: int
    :param carte: tableau représentant la carte des astéroïdes, des '*' pour les asteroides, des '.' pour du vide
    :type carte: list[list[str]]
    """
    if etage == len(carte):
        return "May the force be with you"
    
    if emplacement - 1 >= 0:
        if carte[etage][emplacement - 1] == ".":
            return cafe_asteroide(emplacement -1, etage+1, carte)
        
    if carte[etage][emplacement] == ".":
        return cafe_asteroide(emplacement, etage+1, carte)
    
    if emplacement + 1 <= len(carte[etage]):
        if carte[etage][emplacement + 1] == ".":
            return cafe_asteroide(emplacement + 1, etage+1, carte)
    
    return "I have a bad feeling about this"
    

if __name__ == '__main__':
    h = int(input())
    l = int(input())
    emplacement = int(input())
    carte = [list(input()) for _ in range(h)]
    etage = 1
    print(cafe_asteroide(emplacement, etage, carte))
