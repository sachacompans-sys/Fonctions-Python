prices = ['24,99€', '12,75€', '9,99€']
prices_discounted = []

for price in prices:
    price_without_euro = price.replace('€', ' ')
    price_with_dot = price_without_euro.replace(',', '.')
    price_float = float(price_with_dot)
    prices_discounted.append(price_float - (price_float*15/100))

print(prices_discounted)
