def headline(txt, espace=4):
    length = len(txt) + espace
    center = espace/2
    center = int(center)
    print('-' * length)
    print(f'{' ' * center}{txt.strip().upper()}')
    print('-' * length)

