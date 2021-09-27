def index_of(index, value, lista):
    length = len(lista)
    for y in range(length):
        if lista[y] == value and index != y:
            return True, lista[y]
    return False, False


def valid_type_value(value):
    if type(value) is str:
        return False
    if value < 1:
        return False
    return True


def add_value_repeat(value_repeat, value, result):
    if result:
        value_repeat.add(value)

    if len(value_repeat) > 1:
        return True

    return False


def has_repeat(value_repeat):
    if len(value_repeat) == 0:
        return False
    return list(value_repeat)[0]


def find_duplicate(nums):
    """ Faça o código aqui. """
    if type(nums) is str or len(nums) < 2:
        return False

    length = len(nums)
    value_repeat = set()
    for index in range(length):
        if valid_type_value(nums[index]) is False:
            return False

        result, value = index_of(index, nums[index], nums)

        if add_value_repeat(value_repeat, value, result):
            return False

    return has_repeat(value_repeat)
