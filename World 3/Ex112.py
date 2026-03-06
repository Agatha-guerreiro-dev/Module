from useful.data import validation
from useful.numbers import currency

p = validation.readusd('Type a value: ')
currency.summary(p,15,5)
