print(len('hellloooo'))
print(type(len(str('hellloooo'))))
print(type(print))

quote = 'od ddd dddd br brr brrr'
print(quote.find(' br'))

quote = quote.replace('od', 'ob')
print(quote)

birth_year = int(input('what year were you born: '))
birth_year = 2026 - birth_year

print(f'You are {birth_year} years old')