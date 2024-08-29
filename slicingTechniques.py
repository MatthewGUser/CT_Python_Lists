# [ Task 1 ]

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week = temperatures[7:14]
print(second_week)

# [ Task 2 ]

over_100 = []

for temperature in temperatures:
    if temperature > 100:
        over_100.append(temperature)

print(over_100)

# Alternative:

over_100_alt = temperatures[-6:]
print(over_100_alt)