number = float(input())
bonus = 0

if number <= 100:
    bonus = 5
elif number > 1000:
    bonus = number * 0.10
else:
    bonus = number * 0.20

bonus_2 = 0

if number % 2 == 0:
    bonus_2 = 1
elif number % 5 == 0:
    bonus_2 = 2

total_bonus = bonus + bonus_2
total = number + total_bonus

print(f"{total_bonus:.1f}")
print(f"{total:.1f}")
