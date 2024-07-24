moneyForToys = 0
kidsCount = 0
moneyForSweaters = 0
adultsCount = 0
command = input()

while "Christmas" == command:
    years = int(command)
    if years <= 16:
        moneyForToys += 5
        kidsCount += 1
    else:
        moneyForSweaters += 15
        adultsCount += 1

print(f"Number of adults: {adultsCount}")
print(f"Number of kids: {kidsCount}")
print(f"Money for toys: {moneyForToys}")
print(f"Money for sweaters: {moneyForSweaters}")
