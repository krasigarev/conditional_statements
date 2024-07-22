fruit = input()
day_of_week = input()
quantity = float(input())

result = None

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday":
    if fruit == "banana":
        result = quantity * 2.5
    elif fruit == "apple":
        result = quantity * 1.2
    elif fruit == "orange":
        result = quantity * 0.85
    elif fruit == "grapefruit":
        result = quantity * 1.45
    elif fruit == "kiwi":
        result = quantity * 2.70
    elif fruit == "pineapple":
        result = quantity * 5.50
    elif fruit == "grape":
        result = quantity * 3.85
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        result = quantity * 2.5
    elif fruit == "apple":
        result = quantity * 1.2
    elif fruit == "orange":
        result = quantity * 0.85
    elif fruit == "grapefruit":
        result = quantity * 1.45
    elif fruit == "kiwi":
        result = quantity * 2.70
    elif fruit == "pineapple":
        result = quantity * 5.50
    elif fruit == "grape":
        result = quantity * 3.85

if result:
    print(f"{result:.2f}")
else:
    print("Error")
