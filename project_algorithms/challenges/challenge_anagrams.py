def is_compare(f_string, s_string):
    for letter in f_string:
        for indice in range(len(s_string)):
            if s_string[indice] == letter:
                s_string.pop(indice)
                break


def is_anagram(first_string, second_string):
    f_string = list(first_string)
    s_string = list(second_string)

    if len(f_string) != len(s_string):
        return False

    is_compare(f_string, s_string)

    if len(s_string) == 0:
        return True

    return False


# # s_string = dict(enumerate(list("CORAGEM")))
# # print(s_string)
# print(is_anagram("AMO", "RMA"))
