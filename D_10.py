d = {'!': 1, '@': 2, '#': 3, '$': 4, '%': 5, '^': 6}


def create_list(dict):
    result = []
    for key, value in dict.items():
        result.append(key)
        result.append(value)
    return result


print(create_list(d))
