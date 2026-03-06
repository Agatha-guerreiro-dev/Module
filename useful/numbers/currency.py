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

