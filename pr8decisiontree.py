
print("DECISION TREE AND NAIVE BAYES")

n = int(input("Enter number of training records: "))
data = []

for i in range(n):
    x = float(input("Enter feature value: "))
    label = input("Enter class label: ")
    data.append((x, label))

test = float(input("Enter test feature value: "))

threshold = sum(x for x, y in data) / n

below = [y for x, y in data if x <= threshold]
above = [y for x, y in data if x > threshold]

def majority(labels):
    if not labels:
        return "Unknown"
    return max(set(labels), key=labels.count)

if test <= threshold:
    tree_prediction = majority(below)
else:
    tree_prediction = majority(above)

print("\nDecision Tree-style Prediction:", tree_prediction)

classes = set(y for x, y in data)
scores = {}

for label in classes:
    group = [x for x, y in data if y == label]
    prior = len(group) / n
    distance = sum(abs(x - test) for x in group) / len(group)
    scores[label] = prior / (1 + distance)

prediction = max(scores, key=scores.get)

print("Naive Bayes-style Prediction:", prediction)
print("Class Scores:", scores)
