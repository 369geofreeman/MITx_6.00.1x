# Trees


## Terminology

```
	(A) <---- Node          (A) <--- Root (parent)           (A) <--- Level 1
        / \                     / \                              / \
       /   \ <---- Edge        /   \                            /   \
      /     \                 /     \                          /     \
    (B)     (C)              (B)    (C) <--- Children        (B)     (C) <--- Level 2
   / |      / \                             (Desendent)      /|      / \
  / (E)    /   \                                            / |     /   \
(D)   \   (H)   \                                         (D) (E)  (F)   \
 |    (F)  |    (I)                                                       (G) <--- Level 3
(J)       (G) <--- Leaves   
```


**- Node:** Each circled letter represents a node. A node is any structure that holds data

**- Root node:** The root node is the only node from which all other nodes come from. A tree with an undistinguishable root node cannot be considered as a tree. the root node in our tree is the node (A).

**- Sub-tree:** A sub-tree of a tree with its nodes being a descendant of some other tree. Nodes C, H, G and I form a sub-tree of the original tree consisting of all the nodes

**- Degree:** The number of sub-trees of a given node. A tree sonsisting of only one node has a degree of 0. This one tree node is also considered as a tree by all standards. The degree of node A is 2.

**- Leaf node:** This node is a node with a degree od 0. Nodes J, F, G and I are all leaf nodes.

**- Edge:** The connection between two nodes. An edge can sometimes connect a node to itself, making the edge appear as a loop   

**- Parent:** A node in the tree with other connecting nodes is the parent of those nodes. Node B is the parent of nodes D and E.

**- Child:** This is a node connected to its parent. Nodes B and C are children to node A, the parent and root node.

**- Sibling:** All nodes with the same parent are siblings. This makes the nodes B and C siblings

**- level:** The level of a node is the number of connections from the root node. the root node is at level 0. Nodes B and C are at level 1.

**- Height of a tree:** This is teh number of levels in a tree. Our tree has a height of 4.
**- Depth:** The depth of a node is the number of edges from a root of the tree to that node. the depth of node H is 2


