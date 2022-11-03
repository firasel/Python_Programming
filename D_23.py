exStr = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain"


def subStr(st, end, str):
    return str[st:end+1]


print(subStr(22, 27, exStr))
print(subStr(97, 102, exStr))
