age = float(input())
gender = input()

if age >= 16 and gender == "male":
    print("Mr.")
elif age < 16 and gender == "male":
    print("Master")
elif age >= 16 and gender == "female":
    print("Ms.")
elif age < 16 and gender == "female":
    print("Miss")

if gender == "male":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
else:
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")
