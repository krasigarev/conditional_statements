flowers = input()
count_flower = int(input())
budget = int(input())

price = None

if flowers == "Roses":
    if count_flower <= 80:
        price = count_flower * 5
    elif count_flower > 80:
        price = (count_flower * 5) * 0.90
elif flowers == "Dahlias":
    if count_flower <= 90:
        price = count_flower * 3.80
    elif count_flower > 90:
        price = (count_flower * 3.80) * 0.85
elif flowers == "Tulips":
    if count_flower <= 80:
        price = count_flower * 2.80
    elif count_flower > 80:
        price = (count_flower * 2.80) * 0.85
elif flowers == "Narcissus":
    if count_flower <= 120:
        price = count_flower * 3
    elif count_flower > 120:
        price = (count_flower * 3) * 0.85
elif flowers == "Gladiolus":
    if count_flower <= 80:
        price = count_flower * 2.50
    elif count_flower > 80:
        price = (count_flower * 2.50) * 0.80

difference = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {count_flower} {flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
