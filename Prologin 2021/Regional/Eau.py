def bataille_d_eau(n, m, liste, h, t):
    """
    :param n: Le nombre de villes
    :type n: int
    :param m: Le nombre d'aqueducs entre les villes
    :type m: int
    :param l: Les aqueducs
    :type l: list[list[int]]
    :param h: La ville de Rome
    :type h: int
    :param t: La ville de Tivoli
    :type t: int
    """
    element = []
    element_name =[h,t]
    element.append([h,0])
    element.append([t,0])
    segment = 0
    segment_element = []
    for i in range(len(liste)):
        if liste[i][0] not in element_name:
            element.append([liste[i][0],0])
            element_name.append(liste[i][0])
            
    for i in range(len(liste)):
        for y in range(len(element)):
            if liste[i][0] == element[y][0]:
                element[y][1]+=1
            elif liste[i][1] == element[y][0]:
                element[y][1]+=1
    
    for i in range(len(element)):
        if element[i][1] % 2 != 0:
            segment += 1
            if len(segment_element) < 1 :
                segment_element.append(element[i][0])
    for i in range(len(liste)):
        if segment_element[0] == liste[i][0] or segment_element[0] == liste[i][1]:
            for y in range(len(element)):
                if liste[i][0] == element[y][0] or liste[i][1] == element[y][0]:
                    if element[y][0] != segment_element[0]:
                        if element[y][1] % 2 != 0:
                            segment_element.append(element[y][0])
         
            
            
    print(int(segment - len(segment_element)/2))
    result = ""
    for i in segment_element:
        result += str(i)+" "
    return result
    
#print(bataille_d_eau(3,1,[1, 2],0,2))
      
print(bataille_d_eau(8,9,[[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [5, 7], [6, 7]],0,7))
"""
if __name__ == '__main__':
    n = int(input())
    m = int(input())
    l = [list(map(int, input().split())) for _ in range(m)]
    h = int(input())
    t = int(input())
    print(bataille_d_eau(n, m, l, h, t))
"""
