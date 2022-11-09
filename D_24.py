def nearly_equal(a, b):
    res = False
    if len(a) != len(b)-1:
        return res
    cnt = 0
    i = j = 0
    while (i < len(a) and j < len(b)):
        if a[i] != b[j]:
            cnt += 1
            j += 1
        else:
            i += 1
            j += 1
    if cnt < 2:
        res = True
    return res


print(nearly_equal('perl', 'pearl'))
