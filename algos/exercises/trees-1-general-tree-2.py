# Build below location tree using TreeNode class

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        # Add child to parent node
        child.parent = self
        self.children.append(child)

    def get_level(self):
        # Gets the level of the current node
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, printLevel):
        if self.get_level() > printLevel:
            return

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|-- ' if self.parent else ''

        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(printLevel)


def build_location_tree():
    # Create root node
    root = TreeNode('Global')

    # create India node
    india = TreeNode('India')
    # Add children tp parent Gujarat
    gujarat = TreeNode('Gujarat')
    gujarat.add_child(TreeNode('Ahmedabad'))
    gujarat.add_child(TreeNode('Baroda'))
    # Add children to parent Karataka
    Karnataka = TreeNode('Karnataka')
    Karnataka.add_child(TreeNode('Bangluru'))
    Karnataka.add_child(TreeNode('Mysore'))
    # add children to parent (India)
    india.add_child(gujarat)
    india.add_child(Karnataka)


    # Create usa node
    usa = TreeNode('USA')
    # Add children New Jersey
    new_jersey = TreeNode('New jersey')
    new_jersey.add_child(TreeNode('Princeton'))
    new_jersey.add_child(TreeNode('Trenton'))
    # Add children california
    california = TreeNode('California')
    california.add_child(TreeNode('San francisco'))
    california.add_child(TreeNode('Mountain View'))
    california.add_child(TreeNode('Palo Alto'))
    # Add children to parent (usa)
    usa.add_child(new_jersey)
    usa.add_child(california)

    # Add to root
    root.add_child(india)
    root.add_child(usa)

    return root



if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.print_tree(2)
