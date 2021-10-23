# Python program showing the depth first search for an undirected graph

# Function to return a list containing the DFS traversal of the undirected graph
def dfs_graph(vertices, adj):
    visited = set()
    path = []
    for node in range(vertices):
        if node not in visited:
            dfs(node, visited, path)
    return path

# Recursive function  
def dfs(node, visited, path):
    visited.add(node)
    path.append(node)
    for neighbour in adj[node]:
        if neighbour not in visited:
            dfs(neighbour, visited, path)

print('---------------------------------------------------------------------')
print('\tWelcome to Depth First Search for an undirected graph')
print('---------------------------------------------------------------------\n')
t = int(input("Enter the number of testcases: "))
for _ in range(t):
    print('\n*************** Testcase', _+1, '***************\n')
    vertices, edges = map(int, input("Enter number of vertices & edges (space separated): ").split())
    # Create an adjacency list
    adj = [[] for vertex in range(vertices)]
    for edge in range(edges):
        start, end = map(int, input("Enter edge (space separated): ").split())
        adj[start].append(end)
        adj[end].append(start) # This line should be removed for directed graph
    path = dfs_graph(vertices, adj)
    print("\nDFS Traversal:")
    for node in path:
        print(node, end =' ')
    print()