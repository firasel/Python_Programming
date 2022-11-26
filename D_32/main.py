def half_adder(a, b):
    s = a ^ b
    c = a & b
    print(f'Sum:\t{s}\nCarry:\t{c}')
    return [s, c]


if __name__ == '__main__':
    half_adder(0, 1)


def test_half_adder():
    t1 = half_adder(0, 0)
    assert t1[0] == 0 and t1[1] == 0

    t2 = half_adder(0, 1)
    assert t2[0] == 1 and t2[1] == 0

    t3 = half_adder(1, 0)
    assert t3[0] == 1 and t3[1] == 0

    t4 = half_adder(1, 1)
    assert t4[0] == 0 and t4[1] == 1
