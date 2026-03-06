def money(v):
    return f'US${v:.2f}'


def half(n, show=False):
    value = n / 2
    if show:
        result = money(value)
        return result
    return value


def double(n, show=False):
    value = n * 2
    if show:
        result = money(value)
        return result
    return value


def increase(v, mult, show=False):
    m = (mult / 100) + 1
    value = v * m
    if show:
        result = money(value)
        return result
    return value


def decrease(v, mult, show=False):
    value = v - ((v * mult) / 100)
    if show:
        result = money(value)
        return result
    return value


def summary(v, inc, dec):
    from useful.string import edit
    edit.headline('Value Summary', 40)
    print(f'{"Value analyzed:":<35}{money(v):>7}')
    print(f'{"Double the value:":<35}{double(v,True):>7}')
    print(f'{"Half the value:":<35}{half(v,True):>7}')
    print(f'{f"{inc}% value increase:":<35}{increase(v,inc,True):>7}')
    print(f'{f"{dec}% discount on the value:":<35}{decrease(v,dec,True):>7}')
    text = len('Value Summary') + 40
    print('-' * text)
