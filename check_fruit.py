product = input()

fruit = ("apple", "banana", "kiwi", "cherry", "lemon", "grapes")
vegetable = ("tomato", "cucumber", "pepper", "carrot")

if product in fruit:
    print("fruit")
elif product in vegetable:
    print("vegetable")
else:
    print("Unknown")

is_fruit = product == "banana" or product == "apple" or product == "kiwi" or product == "cherry" or product == "lemon" or product == "grapes"
is_vegetable = product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot"

if is_fruit:
    print("fruit")
elif is_vegetable:
    print("vegetable")
else:
    print("unknown")
