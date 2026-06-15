area = int(input("Enter area of one wall: "))
inside = int(input("Enter inside cost: "))
outside = int(input("Enter outside cost: "))

walls = 8

total_area = area * walls
total_cost = (inside + outside) * walls

print("Total Area =", total_area)
print("Total Cost =", total_cost)