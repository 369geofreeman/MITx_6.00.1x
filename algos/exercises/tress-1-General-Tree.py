# Data structures exercise: General Tree
# Below is the management hierarchy of a company.


# Nilupul (CEO)
# |-- Chinmay (CTO)
#   |-- Vishwa (Infrastructure head)
#      |-- Dhaval (Cloud Manager)
#      |-- Abhijit (App Manager)
#   |-- Aamit (Application head)
# |-- Gels (HR Head)
#   |-- Peter (Recrutement Manager)
#   |-- Waqas (Policy manager)


# Extent tree class built in our main tutorial so that it takes name and designation in data part of TreeNode class. 
# Now extend print_tree function such that it can print either name tree, designation tree or name and designation
# tree.


class TreeNode:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self,printType):
        space = ' ' * self.get_level() * 2
        prefix = space + '|-- ' if self.parent else ''

        if printType == 'name': dataType = self.data[0]
        if printType == 'designation': dataType = self.data[1]
        if printType == 'both': dataType = '{}  ({})'.format(self.data[0], self.data[1])

        print(prefix + dataType)
        if self.children:
            for child in self.children:
                child.print_tree(printType)


def build_management_tree():
    root = TreeNode(['Nilupul', 'CEO'])

    CTO = TreeNode(['Chinmay', 'CTO'])
    IH = TreeNode(['Vishwa', 'Infrastructure head'])
    IH.add_child(TreeNode(['Dhaval', 'Cloud manager']))
    IH.add_child(TreeNode(['Abhijit', 'App Manager']))
    CTO.add_child(IH)

    CTO.add_child(TreeNode(['Aamir', 'Application head']))

    HR_HEAD = TreeNode(['Gels', 'HR Head'])
    HR_HEAD.add_child(TreeNode(['Peter', 'Recrutememt Manager']))
    HR_HEAD.add_child(TreeNode(['Waqas', 'Policy Manager']))

    root.add_child(CTO)
    root.add_child(HR_HEAD)

    return root








if __name__ == '__main__':
    root_node = build_management_tree()
    print('Name hierarchy only:\n')
    root_node.print_tree("name") # prints only name hierarchy
    print('\n------\n')
    print('Designation hierarchy only:\n')
    root_node.print_tree("designation") # prints only designation hierarchy
    print('\n------\n')
    print('Name and designation hierarchy:\n')
    root_node.print_tree("both") # prints both (name and designation) hierarchy
    print('\n------\n')
