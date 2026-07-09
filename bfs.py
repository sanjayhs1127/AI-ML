from collections import deque

# Social Network Graph
graph = {
    "Alice": ["Charlie", "David"],
    "Bob": ["Emma", "Fred"],
    "Charlie": ["Alice", "Emma"],
    "David": ["Alice", "Emma", "Fred"],
    "Emma": ["Bob", "Charlie", "David"],
    "Fred": ["Bob", "David"]
}
# Arrange neighbors alphabetically
for node in graph:
    graph[node].sort()
# ---------------- BFS ----------------
def bfs(graph, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    print("\nBFS Traversal")

    while queue:
        print("Queue:", list(queue))

        node = queue.popleft()
        print("Visited:", node)

        if node == goal:
            break

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("\nShortest Path:")
    print(" -> ".join(path))


# ---------------- DFS ----------------

def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    parent = {start: None}

    print("\nDFS Traversal")

    while stack:
        print("Stack:", stack)

        node = stack.pop()

        if node not in visited:
            visited.add(node)
            print("Visited:", node)

            if node == goal:
                break

            # Reverse alphabetical push
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    if neighbor not in parent:
                        parent[neighbor] = node
                    stack.append(neighbor)

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("\nPath Found:")
    print(" -> ".join(path))


# Driver Code
source = "Alice"
goal = "Bob"

bfs(graph, source, goal)
dfs(graph, source, goal)