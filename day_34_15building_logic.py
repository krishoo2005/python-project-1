capacity = int(input("Enter tank capacity (liters): "))
current = int(input("Current water level: "))
per_min = int(input("Water added per minute: "))

minutes = 0

while current < capacity:
    current = current + per_min
    minutes = minutes + 1

print("Tank full in", minutes, "minutes")
