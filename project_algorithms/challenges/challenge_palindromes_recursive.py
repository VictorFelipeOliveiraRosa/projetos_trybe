def change_letter(low_index, high_index, word):
    word_1 = list(word[1])
    temp = word_1[low_index]
    word_1[low_index] = word_1[high_index]
    word_1[high_index] = temp
    low_index += 1
    high_index -= 1
    word_1 = str("".join(word_1))
    word[1] = word_1
    return low_index, high_index, word


def is_palindrome_recursive(word, low_index, high_index):
    if type(word) != list:
        if type(word) is not str or len(word) == 0:
            return False
        word = [word, word]

    meio = len(word[0]) // 2
    if low_index < meio and high_index >= meio:
        low_index, high_index, word = change_letter(
            low_index, high_index, word
        )

        is_palindrome_recursive(word, low_index, high_index)

    if word[0] == word[1]:
        return True
    return False
