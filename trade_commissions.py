city = input()
sales = float(input())

commission = None

if city == "Sofia":
    if sales <= 500:
        commission = sales * 0.05
    elif sales > 500 and sales <= 1000:
        commission = sales * 0.07
    elif sales > 1000 and sales <= 10000:
        commission = sales * 0.08
    elif sales > 10000:
        commission = sales * 0.12
elif city == "Varna":
    if sales <= 500:
        commission = sales * 0.045
    elif sales > 500 and sales <= 1000:
        commission = sales * 0.075
    elif sales > 1000 and sales <= 10000:
        commission = sales * 0.10
    elif sales > 10000:
        commission = sales * 0.13
elif city == "Plovdiv":
    if sales <= 500:
        commission = sales * 0.055
    elif sales > 500 and sales <= 1000:
        commission = sales * 0.08
    elif sales > 1000 and sales <= 10000:
        commission = sales * 0.12
    elif sales > 10000:
        commission = sales * 0.145

if commission:
    print(f"{commission:.2f}")
else:
    print("Error")
