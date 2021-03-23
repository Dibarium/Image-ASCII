def trouver_lettre(t, s):
    """
    :param t: taille de la séquence
    :type t: int
    :param s: liste des entiers que Hermès a sorti
    :type s: list[int]
    """
    letter = s[0]
    if letter < 65 or letter > 90:
        return " "
    for i in range(1,t):
        if s[i]>26:
            s[i] = s[i]-26
        letter += s[i]
    
    return chr((letter-65)%26+65)

if __name__ == '__main__':
    t = int(input())
    s = list(map(int, input().split()))
    print(trouver_lettre(t, s))