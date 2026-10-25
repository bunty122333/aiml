
from collections import deque

graph = {}

n = int(input("Enter number of locations: "))

for i in range(n):
    node = input("Enter location name: ").strip()
    graph[node] = []

e = int(input("Enter number of connections: "))

for i in range(e):
    a, b = input("Enter connection (A B): ").split()

    if a not in graph or b not in graph:
        print("Invalid location!")
        raise SystemExit

    graph[a].append(b)
    graph[b].append(a)

start = input("Enter starting location: ").strip()
goal = input("Enter destination: ").strip()

if start not in graph or goal not in graph:
    print("Invalid starting location or destination!")
    raise SystemExit

def bfs(start, goal):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(path + [neighbour])

    return None

def dfs(start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(path + [neighbour])

    return None

print("\nBFS Path:", bfs(start, goal))
print("DFS Path:", dfs(start, goal))
