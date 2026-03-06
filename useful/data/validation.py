def readusd(str):
    while True:
        currency = input(str).strip().replace(',','.')
        try:
            return float(currency)
        except ValueError:
            print('\033[31m Error, please type a valid value!\033[m')


def readbrl(str):
    import locale
    try:
        locale.setlocale(locale.LC_NUMERIC, 'pt_BR.UTF-8')
    except locale.Error:
        locale.setlocale(locale.LC_NUMERIC, 'Portuguese_Brazil')
    while True:
        currency = input(str).strip()
        try:
            return locale.atof(currency)
        except ValueError:
            print('\033[31m Error, please type a valid value!\033[m')

