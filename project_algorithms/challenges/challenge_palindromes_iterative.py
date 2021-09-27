def is_palindrome_iterative(word):
    if type(word) is not str or len(word) < 2:
        return False
    copy_word = word

    copy_word = word[::-1]

    if copy_word == word:
        return True

    return False


# is_palindrome_iterative("VICTOR")
