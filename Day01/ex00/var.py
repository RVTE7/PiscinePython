def my_var():
    a = 42
    print(f"{a} has a type {type(a)}")

    b = '42'
    print(f"{b} has a type {type(b)}")

    c = "quarante-deux"
    print(f"{c} has a type {type(c)}")

    d = 42.0
    print(f"{d} has a type {type(d)}")

    e = 42 < 43
    print(f"{e} has a type {type(e)}")

    f = [42]
    print(f"{f} has a type {type(f)}")

    g = {42: 42}
    print(f"{g} has a type {type(g)}")

    h = (42,)
    print(f"{h} has a type {type(h)}")

    i = set()
    print(f"{i} has a type {type(i)}")

if __name__ == '__main__':
    my_var()