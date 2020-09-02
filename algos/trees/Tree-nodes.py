# Tree Nodes


# The nodes that make up a tree need to contain data about the parent-child relationship 

class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


# Create a few nodes

n1 = Node("Root node")
n2 = Node("left child node")
n3 = Node("Right child node")
n4 = Node("Left grandchild node")


# Connect the nodes to each other

n1.left_child = n2
n1.right_child = n3
n2.left_child = n4

# Once we have our tree structure set up, we are ready to traverse it. 
# We shall traverse the left sub-tree. We print out the node and move down the tree to the next left node. 
# We keep doing this until we have reached the end of the left sub- tree:


current = n1
while current:
    print(current.data)
    current = current.left_child
