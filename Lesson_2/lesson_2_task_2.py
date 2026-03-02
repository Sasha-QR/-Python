def is_year_leap(year):
    return True if year % 4 == 0 else False


years = int(input("Введите год: "))
result = is_year_leap(years)
print(f"год {years} - {result}")
