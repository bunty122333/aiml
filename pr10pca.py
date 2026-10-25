
import math

print("PRINCIPAL COMPONENT ANALYSIS")

n = int(input("Enter number of records: "))
data = []

for i in range(n):
    row = list(map(float, input(
        "Enter two feature values: ").split()))

    if len(row) != 2:
        print("Enter exactly two values.")
        raise SystemExit

    data.append(row)

mean1 = sum(row[0] for row in data) / n
mean2 = sum(row[1] for row in data) / n

centered = [[row[0] - mean1, row[1] - mean2]
            for row in data]

var1 = sum(row[0] ** 2 for row in centered) / n
var2 = sum(row[1] ** 2 for row in centered) / n
cov = sum(row[0] * row[1] for row in centered) / n

angle = 0.5 * math.atan2(2 * cov, var1 - var2)
component = [math.cos(angle), math.sin(angle)]

reduced = [row[0] * component[0] +
           row[1] * component[1] for row in centered]

print("\nOriginal Feature Count: 2")
print("Reduced Feature Count: 1")
print("Principal Component:", [round(x, 3) for x in component])
print("Reduced Data:", [round(x, 3) for x in reduced])
