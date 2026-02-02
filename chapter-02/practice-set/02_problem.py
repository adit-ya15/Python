from datetime import date

today = date.today()
name = input("Enter your name: ")

letter = f'''
Dear {name}
your are selected at
{today}
'''
print(letter)