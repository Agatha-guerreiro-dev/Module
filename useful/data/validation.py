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


def readint(str):
    while True:
        try:
            n = int(input(str).strip())
        except ValueError:
            print('\033[31m Error, please type an integer number!\033[m')
        except KeyboardInterrupt:
            print('\033[31m Error, user chose not to enter data.\033[m')
        else:
            return n


def readfloat(str):
    while True:
        try:
            n = float(input(str).strip().replace(',','.'))
        except ValueError:
            print('\033[31m Error, please type a floating point number!\033[m')
        except KeyboardInterrupt:
            print('\033[31m Error, user chose not to enter data.\033[m')
        else:
            return n


def sitevalid(txt):
    from urllib import request, error, parse
    while True:
        url = input(txt).strip()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        domain = parse.urlparse(url).netloc
        site_name = domain.replace('www.', '').split('.')[0].capitalize()
        my_header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        try:
            req = request.Request(url, headers=my_header)
            site = request.urlopen(req)
        except error.HTTPError:
            print('\033[31m The site exists, but the connection was refused (HTTP Error).\033[m')
        except error.URLError:
            print('\033[31m The site is currently unavailable or the URL is invalid.\033[m')
        except ValueError:
            print('\033[31m Error, please enter a valid URL format (e.g., http://www.site.com).\033[m')
        else:
            print(f'\033[32m Site {site_name} accessible! Request approved.\033[m')
            break


def readstr(txt):
    while True:
        try:
            n = str(input(txt).strip())
        except ValueError:
            print('\033[31m Error, please type a valid string!\033[m')
        except KeyboardInterrupt:
            print('\033[31m Error, user chose not to enter data.\033[m')
        else:
            return n