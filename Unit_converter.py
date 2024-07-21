meters = float(input())
input_units = input()
output_units = input()

mm = 1000
cm = 100
m = 1

if input_units == "mm" and output_units == "m":
    result = (meters / mm) * m
elif input_units == "mm" and output_units == "cm":
    result = (meters / mm) * cm
elif input_units == "mm" and output_units == "mm":
    result = (meters / mm) * mm
elif input_units == "cm" and output_units == "m":
    result = (meters / cm) * m
elif input_units == "cm" and output_units == "cm":
    result = (meters / cm) * cm
elif input_units == "cm" and output_units == "mm":
    result = (meters / cm) * mm
elif input_units == "m" and output_units == "m":
    result = (meters / m) * m
elif input_units == "m" and output_units == "cm":
    result = (meters / m) * cm
elif input_units == "m" and output_units == "mm":
    result = (meters / m) * mm

print(f"{result:.3f}")
