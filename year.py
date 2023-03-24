year = int(input("Введите год: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    dm = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    dm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

result = 0

for month in range(12):
    days = dm[month]
    for day in range(1, days+1):
        num = [int(d) for d in str(day)]
        numsum = sum(num)
        result += numsum
        

print(f"Общая сумма цифр всех дат для каждого месяца всех дней в году: {result}")