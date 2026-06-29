feet = int(input("Enter feet: "))
inch = int(input("Enter inches: "))

total_inch = (feet * 12) + inch
cm = total_inch * 2.54
meter = cm / 100

print("Meter =", meter)
print("Centimeter =", cm)