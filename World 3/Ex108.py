"""
Challenge:
Adapt the code from challenge 107, creating an additional function called currency() inside your module.
This function must be able to display the numeric results as a formatted monetary string
"""
from useful.numbers import currency

p = float(input('Product price US$: ').replace(',', '.'))
print(f'The half of {currency.money(p)} is {currency.half(p,show=True)}')
print(f'The double of {currency.money(p)} is {currency.double(p,show=True)}')
print(f'Rising 10% of the product value, we have {currency.increase(p, 10,True)}')
print(f'Decreasing 13% of the product value, we have {currency.decrease(p, 13,True)}')
