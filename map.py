# Map(): Pass in a function and an iterable. Map will then create an object that has the output obtained from running 
# each iterable element through the function.

king_county_sales_tax = .087
cars = [28000, 19000, 21678, 20100]


def get_total_price(car):
    return car * (1 + king_county_sales_tax)


total_prices = map(get_total_price, cars)

print(list(total_prices))
