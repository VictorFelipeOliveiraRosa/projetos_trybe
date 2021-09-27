def validy_period(time_period, target_time):
    if time_period[0] == target_time or time_period[1] == target_time:
        return 1
    elif time_period[0] <= target_time and target_time <= time_period[1]:
        return 1
    return 0


def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if type(target_time) is not int:
        return None
    contador = 0
    for time_period in permanence_period:
        if type(time_period[0]) is not int or type(time_period[1]) is not int:
            return None
        contador += validy_period(time_period, target_time)
    if contador > 0:
        return contador
    return None


permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
r = study_schedule(permanence_period, 1)
print(r)
