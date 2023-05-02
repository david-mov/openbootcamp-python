countries = input('Enter the country names separated by commas: ')
countries_set = sorted(set(countries.split(',')))
print('List of countries alphabetically ordered and without duplicates: \n',
    countries_set)
