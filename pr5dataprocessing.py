
data = []

n = int(input("Enter number of records: "))

for i in range(n):
    name = input("Enter name: ")
    value = input("Enter numeric value (blank if missing): ")
    city = input("Enter city: ")

    if value.strip() == "":
        value = None
    else:
        value = float(value)

    data.append([name, value, city])

print("\nOriginal Data:")
for row in data:
    print(row)

values = [row[1] for row in data if row[1] is not None]

if not values:
    print("No numeric values available.")
    raise SystemExit

mean = sum(values) / len(values)

for row in data:
    if row[1] is None:
        row[1] = mean

minimum = min(row[1] for row in data)
maximum = max(row[1] for row in data)

cities = sorted(set(row[2] for row in data))
encoding = {city: i for i, city in enumerate(cities)}

print("\nProcessed Data:")
for row in data:
    normalized = (
        (row[1] - minimum) / (maximum - minimum)
        if maximum != minimum else 0
    )
    print(row[0], "Value:", row[1],
          "Normalized:", round(normalized, 2),
          "City Code:", encoding[row[2]])

split = int(0.8 * n)
print("\nTraining records:", data[:split])
print("Testing records:", data[split:])
print("City encoding:", encoding)
