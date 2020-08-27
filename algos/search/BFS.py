# BFS (Breadth First Search)

# Breadth First Search Implementation in Python,
# Finding shortest distance and path of any node from source node in a Graph.

# (B)--(A)   (E)---(G)
#  |    |   / |     |
#  |    |  /  |     |
# (C)  (D)/--(F)---(H)


from queue import Queue

adj_lst = {
    "A": ["B","D"],
    "B": ["A","C"],
    "C": ["B"],
    "D": ["A","E","F"],
    "E": ["D","F","G"],
    "F": ["D","E","H"],
    "G": ["E","H"],
    "H": ["G","F"]
}


# BFS code

visited= {}
level = {} # distance dictonary
parent = {}
bfs_traversal_output = []
queue = Queue()


# Set all the entries for the graph
for node in adj_lst.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1 # infinity


# Set the source node/vertex
s = "A"
visited[s] = True
level[s] = 0
queue.put(s)


# Start the search
while not queue.empty():
    u = queue.get()
    bfs_traversal_output.append(u)

    for v in adj_lst[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u]+1
            queue.put(v)

# Output of the BFS
print(bfs_traversal_output)

# Shortest distance of all nodes from source node
print(level)

# Distance of single element from source
print(level["E"])

# Shortest node of any path from source nbode
v = "G"
path = []
while v != None:
    path.append(v)
    v = parent[v]
path.reverse()
print(path)





