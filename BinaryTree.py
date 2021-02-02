
class Node():

    def __init__(self, data, height):
        self.data = data
        self.right = None
        self.left = None
        self.height = height

    def add_left_node(self):
        self.left = Node("branch", self.height + 1)

    def add_right_node(self):
        self.right = Node("branch", self.height + 1)




class binTree():

    def __init__(self):
        self.root = Node("root", 0)
        self.max_height = 0

    def get_max_length(self, Node):
        if Node.right is not None:
            if Node.right.height > self.max_height:
                self.max_height = Node.right.height
            self.get_max_length(Node.right)

        if Node.left is not None:
            if Node.left.height > self.max_height:
                self.max_height = Node.left.height
            self.get_max_length(Node.left)

    def tree_balance(self, Node):
        if self.get_balance(Node):
            self.tree_balance(Node.right)
            self.tree_balance(Node.left)
            return True
        elif Node.left is None and Node.right is None:
            return True
        return False


    def get_balance(self, Node):
        if Node.right is not None and Node.left is not None:
            return True
        else:
            return False




tree = binTree()
tree.root.add_left_node()
tree.root.add_right_node()
tree.root.right.add_right_node()
tree.root.right.add_left_node()

tree.get_max_length(tree.root)

print("Max length is {}".format(tree.max_height))

if tree.tree_balance(tree.root) == True:
    print("Balanced")
else:
    print("Not Balanced")



