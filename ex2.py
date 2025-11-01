# Lab 9: Graph Representation and Traversals
# Objective: Implement graph representations and traversals (CO1, CO2)

def add_edge(graph, u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)
def dfs(graph, start, visited):
    visited.append(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
def bfs(graph, start):
    visited = []
    queue = []
    visited.append(start)
    queue.append(start)
    while len(queue) > 0:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
graph = {}
n = int(input("Enter size (number of edges): "))
print("Enter edges (like A B for an edge between A and B):")
for i in range(n):
    u, v = input().split()
    add_edge(graph, u, v)
print("\nGraph Representation (Adjacency List):")
for node in graph:
    print(node, "->", graph[node])
start_node = input("\nEnter starting node for DFS: ")
print("DFS Traversal:", end=" ")
dfs(graph, start_node, [])
start_node = input("\n\nEnter starting node for BFS: ")
print("BFS Traversal:", end=" ")
bfs(graph, start_node)
print()
