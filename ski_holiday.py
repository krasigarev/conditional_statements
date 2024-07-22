count_day = int(input())
type_room = input()
rating = input()

day = count_day - 1
sleeping = None

if type_room == "room for one person":
    if day < 10:
        sleeping = day * 25
        if rating == "positive":
            sleeping = sleeping * 1.25
        else:
            sleeping = sleeping * 0.9
    elif day <= 10 or day <= 15:
        sleeping = day * 18
        if rating == "positive":
            sleeping = sleeping * 1.25
        else:
            sleeping = sleeping * 0.9
    elif day > 15:
        sleeping = day * 18
        if rating == "positive":
            sleeping = sleeping * 1.25
        else:
            sleeping = sleeping * 0.9
elif type_room == "apartment":
    if day < 10:
        sleeping = day * 25
        sleeping = sleeping * 0.70
        if rating == "positive":
            sleeping = sleeping * 1.25
        else:
            sleeping = sleeping * 0.9
    elif day <= 10 or day <= 15:
        sleeping = day * 25
        sleeping = sleeping * 0.65
        if rating == "positive":
            sleeping = sleeping * 1.25
        else:
            sleeping = sleeping * 0.9
    elif day > 15:
        sleeping = day * 25
        sleeping = sleeping * 0.50
        if rating == "positive":
            sleeping = sleeping * 1.25
        else:
            sleeping = sleeping * 0.9

elif type_room == "president apartment":
    if day < 10:
        sleeping = day * 35
        sleeping = sleeping * 0.90
        if rating == "positive":
            sleeping = sleeping * 1.25
        else:
            sleeping = sleeping * 0.9
    elif day <= 10 or day <= 15:
        sleeping = day * 35
        sleeping = sleeping * 0.85
        if rating == "positive":
            sleeping = sleeping * 1.25
        else:
            sleeping = sleeping * 0.9
    elif day > 15:
        sleeping = day * 35
        sleeping = sleeping * 0.80
        if rating == "positive":
            sleeping = sleeping * 1.25
        else:
            sleeping = sleeping * 0.9

if sleeping:
    print(f"{sleeping:.2f}")
