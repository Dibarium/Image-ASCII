def meteorite_vagues_vent(s, t):
    """
    :param s: l'action de l'être céleste 1
    :type s: int
    :param t: l'action de l'être céleste 2
    :type t: int
    """
    
    if s == t:
        print(0)
    elif s == 0:
        if t == 1:
            print(2)
        else:
            print(1)
    elif s == 1:
        if t == 2:
            print(2)
        else:
            print(1)
    elif s == 2:
        if t == 0:
            print(2)
        else:
            print(1)
            


if __name__ == '__main__':
    s = int(input())
    t = int(input())
    meteorite_vagues_vent(s, t)
