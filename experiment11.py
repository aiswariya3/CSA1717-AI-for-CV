def is_safe(node, graph, colors, color, c):
    for neighbor in graph[node]:
        if colors[neighbor] == c:
            return False
    return True

def graph_coloring_util(graph, m, colors, node):
    if node == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(node, graph, colors, m, c):
            colors[node] = c
            if graph_coloring_util(graph, m, colors, node + 1):
                return True
            colors[node] = 0 

    return False

def map_coloring(graph, m):
    colors = [0] * len(graph)
    if not graph_coloring_util(graph, m, colors, 0):
        print("No solution exists.")
        return None
    else:
        print("Coloring solution:", colors)
        return colors
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}
m = 3

map_coloring(graph, m)
