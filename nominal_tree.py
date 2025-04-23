class TreeNode:
    def __init__(self, step, id):
        self.parents = []
        self.step = step
        self.up_child = None
        self.down_child = None
        self.id = id
        self.value = 0
    
    def add_up_child(self, child):
        self.up_child = child
        child.add_parent(self)
    
    def add_down_child(self, child):
        self.down_child = child
        child.add_parent(self)

    def get_up_child(self):
        return self.up_child
    
    def get_down_child(self):
        return self.down_child

    def get_children(self):
        return self.down_child, self.up_child
    
    def add_parent(self, parent):
        if parent in self.parents:
            return
        self.parents.append(parent)

    def traverse_tree(self, func):
        current_nodes = [self]
        while len(current_nodes) > 0:
            next_nodes = []
            for node in current_nodes:
                func(node)
                if node.up_child is not None:
                    next_nodes.append(node.up_child)
                if node.down_child is not None:
                    next_nodes.append(node.down_child)
            current_nodes = set(next_nodes)

class NominalTree:
    def naming(self):
        for i in range(0, 10000):
            yield str(i)
    
    def build_binomial_tree(self, steps):
        naming = self.naming()
        first_node = TreeNode(0, next(naming))
        current_nodes = [first_node]
        for i in range(steps - 1):
            next_nodes = []
            previous_up_node = None
            for node in current_nodes:
                if previous_up_node is not None:
                    down_child = previous_up_node
                    node.add_down_child(down_child)
                else:
                    down_child = TreeNode(i + 1, next(naming))
                    next_nodes.append(down_child)
                up_child = TreeNode(i + 1, next(naming))
                next_nodes.append(up_child)
                node.add_up_child(up_child)
                node.add_down_child(down_child)
                previous_up_node = up_child
            current_nodes = next_nodes
        return first_node
    
    def print_tree(self, tree):
        print("\nTree:")
        current_nodes = [tree]
        while len(current_nodes) > 0:
            next_nodes = []
            for node in current_nodes:
                print(str(node.value) + " (" + ",".join([parent.id for parent in node.parents]) + ")", end=" ")
                if node.up_child is not None:
                    next_nodes.append(node.up_child)
                if node.down_child is not None:
                    next_nodes.append(node.down_child)
            print()
            current_nodes = set(next_nodes)

#NominalTree().print_tree(NominalTree().build_binomial_tree(4))