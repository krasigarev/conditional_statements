x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

if x1 < x2 and y1 < y2 and x >= x1 and x <= x2 and y >= y1 and y <= y2:
    print("inside")
else:
    print("outside")

if (x1 <= x) and (x <= x2) and (y1 <= y) and (y <= y2):
    print("inside")
else:
    print("outside")
