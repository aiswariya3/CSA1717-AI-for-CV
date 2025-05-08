# Sample graph represented using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Visited set to keep track of visited nodes
visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

# Start DFS from node 'A'
print("DFS Traversal starting from node A:")
dfs('A')
