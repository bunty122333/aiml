
print("CLASSIFICATION AND PARAMETER SEARCH")

n = int(input("Enter number of training records: "))
data = []

for i in range(n):
    x = float(input("Enter feature value: "))
    label = int(input("Enter class (0 or 1): "))
    data.append((x, label))

test = float(input("Enter test feature value: "))

class0 = [x for x, y in data if y == 0]
class1 = [x for x, y in data if y == 1]

if class0 and class1:
    boundary = (sum(class0) / len(class0) +
                sum(class1) / len(class1)) / 2
    svm_prediction = 1 if test > boundary else 0
else:
    boundary = None
    svm_prediction = data[0][1]

print("\nSVM-style Prediction:", svm_prediction)

thresholds = [
    sum(x for x, y in data) / n,
    sorted(x for x, y in data)[n // 2]
]

votes = []

for threshold in thresholds:
    lower = [y for x, y in data if x <= threshold]
    upper = [y for x, y in data if x > threshold]
    group = lower if test <= threshold else upper

    if group:
        votes.append(max(set(group), key=group.count))
    else:
        votes.append(0)

print("Random Forest-style Prediction:",
      max(set(votes), key=votes.count))

print("AdaBoost: Combine weak classifiers using weighted voting.")
print("Base predictions:", votes)

print("\nParameter Search")
best_threshold = None
best_correct = -1

for threshold in sorted(set(x for x, y in data)):
    correct = 0

    for x, label in data:
        prediction = 1 if x > threshold else 0
        if prediction == label:
            correct += 1

    print("Threshold:", threshold, "Correct:", correct)

    if correct > best_correct:
        best_correct = correct
        best_threshold = threshold

print("Best Threshold:", best_threshold)
print("Best Training Accuracy:", round(best_correct / n, 2))
