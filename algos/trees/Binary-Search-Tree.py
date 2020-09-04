# Binary Search Tree (BST)

# A binary tree is one in which each node has a maximum of two children

# All nodes on the left side must be less than the root node and all the nodes on the right side must be greater than the root node ot quallify as a BST

# an example with (5) being thne root node

#    (5)       
#    /  \      
#  (3)  (7)    
#       / \    
#     (6) (9)  
#             
# -------------

# Each child is identified as being the right or left child of its parent. 
# Since the parent node is also a node by itself, each node will hold a reference to a 
# right and left node even if the nodes do not exist.



# Implimentation

class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

class Tree:
    def __init__(self):
        self.root_node = None

    def find_min(self):
        # Find the minimum node. O(n)
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current

    def find_max(self):
        # Find the max node. O(n)
        current = self.root_node
        while current.right_child:
            current = current.right_child
        return current

    def insert(self,data):
        # Insert a node. O(n)
        node = Node(data)
        if self.root_node == None:
            self.root_node = node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < current.data:
                    current = currernt.left_child
                    if current == None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current == None:
                        parent.right_child = node
                        return

    def get node_with_parent(self, data):
        parent = None
        current = self.root_node
        if current == None:
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child
        return (parent, current)


    def remove(self, data):
        # remove a node from the tree: O(n)
        parent, node = self .get_node_with_parent(data)

        if parent == None and node = None:
            return False
        # Get children count
        children_count = 0
        if node.left_child and node.right_child:
            children_count = 2
        elif (node.left_child == None) and (node.right_child == None):
            children_count = 0
        else:
            children_count = 1

        if children_count = 0:
            if parent:
                if parent.right_child == node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root_node = None
        elif children_count == 1:
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child
            if parent:
                if parent.left_child == node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                self.root_node = next_node

        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child
            node.data = leftmost_node.data

        if parent_of_leftmost_node.left_child == leftmost_node:
            parent_of_leftmost_node.left_child = leftmost_node.right_child
        else:
            parent_of_leftmost_node.right_child = leftmost_node.right_child



