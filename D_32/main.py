def half_adder(a, b):
    s = a ^ b
    c = a & b
    print(f'Sum:\t{s}\nCarry:\t{c}')
    return [s, c]


if __name__ == '__main__':
    half_adder(0, 1)
