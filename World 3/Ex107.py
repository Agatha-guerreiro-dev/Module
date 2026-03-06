"""
Exercise 107:
Create a module called currency.py
that has the built-in functions increase(), decrease(), double() and half().
Also make a program that imports this module and uses some of these functions.
"""
from useful.numbers import currency

p = float(input('Product price US$: ').replace(',', '.'))
print(f'The half of {p} is {currency.half(p)}')
print(f'The double of {p} is {currency.double(p)}')
print(f'Rising 10% of the product value, we have {currency.increase(p, 10)}')
print(f'Decreasing 13% of the product value, we have {currency.decrease(p, 13)}')
