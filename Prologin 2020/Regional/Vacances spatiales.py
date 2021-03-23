def vacances_spatiales(p, d, mn, calendar):
    """
    :param p: le nombre de jours durant lesquels Chewbacca peut partir
    :type p: int
    :param d: le nombre de jours total minimun que Chewie veut passer avec sa famille
    :type d: int
    :param mn: le minimum de jours consécutifs pour un voyage
    :type mn: int
    :param calendar: les jours de la période donnée
    :type calendar: list[int]
    """
    count = 0
    daysf = 0
    for i in range(len(calendar)):
        if calendar[i] == 0:
            count += 1
        else:
            if count >= mn:
                daysf += count
            count = 0
    if count >= mn:
        daysf += count
    if daysf >= d:
        return 1
    else:
        return 0

if __name__ == '__main__':
    p = int(input())
    d = int(input())
    mn = int(input())
    calendar = list(map(int, input().split()))
    print(vacances_spatiales(p, d, mn, calendar))
