needed_money = float(input())
owned_money = float(input())

days_counter = 0
spending_counter = 0

while True:
    text = input()
    money_sum = float(input())

    days_counter += 1

    if text == "spend" and days_counter < 5:
        if owned_money <= money_sum:
            owned_money = 0
        else:
            owned_money -= money_sum
    elif text == "spend" and days_counter >= 5:
        print(f"You can't save the money.")
        print(days_counter)
        break

    if text == "save":
        owned_money += money_sum

    if owned_money >= needed_money:
        print(f'You saved the money for {days_counter} days.')
        break
