
points = list(map(float, input(
    "Enter data points separated by spaces: ").split()))

k = int(input("Enter number of clusters: "))

if k < 1 or k > len(points):
    print("Invalid number of clusters!")
    raise SystemExit

centers = points[:k]

for iteration in range(10):
    clusters = [[] for i in range(k)]

    for point in points:
        nearest = min(range(k),
                      key=lambda i: abs(point - centers[i]))
        clusters[nearest].append(point)

    for i in range(k):
        if clusters[i]:
            centers[i] = sum(clusters[i]) / len(clusters[i])

print("\nK-Means Clusters:")
for i, cluster in enumerate(clusters):
    print("Cluster", i + 1, ":", cluster)

print("Centroids:", centers)

print("\nHierarchical Clustering")
groups = [[point] for point in points]

while len(groups) > 1:
    best_i, best_j = 0, 1
    best_distance = float("inf")

    for i in range(len(groups)):
        for j in range(i + 1, len(groups)):
            distance = min(abs(a - b)
                           for a in groups[i]
                           for b in groups[j])

            if distance < best_distance:
                best_distance = distance
                best_i, best_j = i, j

    print("Merge", groups[best_i], "and", groups[best_j])

    merged = groups[best_i] + groups[best_j]
    groups.pop(best_j)
    groups.pop(best_i)
    groups.append(merged)

print("Final Cluster:", groups)
