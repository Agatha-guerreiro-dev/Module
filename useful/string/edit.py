def headline(txt, espace=4, f_line=False):
    length = len(txt) + espace
    center = espace/2
    center = int(center)
    if f_line:
        return print('-' * length)
    print('-' * length)
    print(f'{' ' * center}{txt.strip().upper()}')
    print('-' * length)


def menumaker(title, espace=4,*txt):
    length = len(title) + espace
    center = espace / 2
    center = int(center)
    print('-' * length)
    print(f'{' ' * center}{title.strip().upper()}')
    print('-' * length)
    for pos, t in enumerate(txt):
        index = pos + 1
        print(f'\033[33m{index}\033[m - \033[34m {t.strip().title()}\033[m')
    print('-' * length)

