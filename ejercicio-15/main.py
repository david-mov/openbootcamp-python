from functools import reduce

def odd_number_sum(list):
    odd_numbers = filter(lambda n: n % 2, list)
    return reduce(lambda a, b: a + b, odd_numbers)

# tests
print(odd_number_sum(range(1, 8))) # 1+3+5+7 = 16
print(odd_number_sum(range(1, 14))) # 1+3+5+7+9+11+13 = 49