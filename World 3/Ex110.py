from useful.numbers import currency

p = float(input('Type the price: ').replace(',','.'))
currency.summary(p,80,35)
