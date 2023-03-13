is_leap_year = lambda y: True if not y % 4 and (y % 100 or not y % 400) else False

# tests

print(is_leap_year(2024)) # True
print(is_leap_year(2028)) # True
print(is_leap_year(2100)) # False
print(is_leap_year(2200)) # False