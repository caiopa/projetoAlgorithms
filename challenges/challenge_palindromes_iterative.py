def is_palindrome_iterative(word):
    if not word:
        return False

    if word == word[::-1]:
        return True
    return False
