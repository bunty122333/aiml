
import math

print("LOGISTIC REGRESSION AND KNN")

n = int(input("Enter number of training records: "))
data = []

for i in range(n):
    x = float(input("Enter feature value: "))
    label = int(input("Enter class (0 or 1): "))
    data.append((x, label))

test = float(input("Enter test feature value: "))

mx = sum(x for x, y in data) / n
my = sum(y for x, y in data) / n

den = sum((x - mx) ** 2 for x, y in data)
slope = sum((x - mx) * (y - my)
            for x, y in data) / den if den else 0
intercept = my - slope * mx

z = slope * test + intercept
z = max(-500, min(500, z))
probability = 1 / (1 + math.exp(-z))

print("\nLogistic-style Probability:", round(probability, 3))
print("Predicted Class:", 1 if probability >= 0.5 else 0)

k = int(input("Enter K for KNN: "))
k = max(1, min(k, n))

nearest = sorted(data, key=lambda row: abs(row[0] - test))[:k]
votes = sum(label for x, label in nearest)

print("Nearest Neighbours:", nearest)
print("KNN Predicted Class:",
      1 if votes > k / 2 else 0)
