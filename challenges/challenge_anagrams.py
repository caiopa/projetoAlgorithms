

def merge_sort(str: str,):
    if len(str) <= 1:
        return str

    mid = len(str)//2
    left = str[:mid]
    right = str[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left: str, right: str):
    res = []
    left_list = list(left)
    right_list = list(right)
    while len(left_list) > 0 and len(right_list) > 0:
        if left_list[0] < right_list[0]:
            res.append(left_list[0])
            left_list = left_list[1:]
        else:
            res.append(right_list[0])
            right_list = right_list[1:]

    res += right_list
    res += left_list

    result = "".join(res)
    return result


def is_anagram(first_string, second_string):
    str1 = merge_sort(first_string.lower())
    str2 = merge_sort(second_string.lower())

    if first_string == '' or second_string == '':
        return (str1, str2, False)

    if len(first_string) != len(second_string):
        return (str1, str2, False)

    return (str1, str2, str1 == str2)
