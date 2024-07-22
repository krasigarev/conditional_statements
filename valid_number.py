number = int(input())

if number == 0:
    pass
elif number in range(100, 200):
    pass
else:
    print("invalid")

if (number >= 100 and number <= 200) or number == 0:
    pass
else:
    print("invalid")

if not ((number >= 100 and number <= 200) or number == 0):
    print("invalid")
