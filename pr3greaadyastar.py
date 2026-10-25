
import heapq

graph = {}
n = int(input("Enter number of locations: "))

for i in range(n):
    node = input("Enter location name: ")
    graph[node] = []

e = int(input("Enter number of connections: "))

for i in range(e):
    a, b, cost = input("Enter connection (A B cost): ").split()
    cost = int(cost)
    graph[a].append((b, cost))
    graph[b].append((a, cost))

h = {}
for node in graph:
    h[node] = int(input("Enter heuristic for " + node + ": "))

start = input("Enter starting location: ")
goal = input("Enter destination: ")

if start not in graph or goal not in graph:
    print("Invalid location!")
    raise SystemExit

def greedy():
    pq = [(h[start], [start])]
    visited = set()

    while pq:
        _, path = heapq.heappop(pq)
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbour, cost in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(
                        pq, (h[neighbour], path + [neighbour])
                    )
    return None

def astar():
    pq = [(h[start], 0, [start])]
    best = {start: 0}

    while pq:
        _, cost, path = heapq.heappop(pq)
        node = path[-1]

        if cost != best.get(node):
            continue

        if node == goal:
            return path, cost

        for neighbour, edge_cost in graph[node]:
            new_cost = cost + edge_cost

            if new_cost < best.get(neighbour, float("inf")):
                best[neighbour] = new_cost
                heapq.heappush(
                    pq, (new_cost + h[neighbour],
                         new_cost, path + [neighbour])
                )
    return None

print("Greedy Path:", greedy())
print("A* Path and Cost:", astar())
