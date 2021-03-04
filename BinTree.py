import random
#TODO make sure to flatten binary tree to linked list
#TODO find least common ancestor of binary tree nods
#TODO Convert a binary tree to its sum tree(each node is the sum of its children)
# 1--2---5--6--19--0--2-20-13-15-3-5-32-1-3-7-6-8
#16
class Node:
    data = 0
    def __init__(self, data):
        self.data = int(data)
        self.right = None
        self.left = None

    def add_left(self,data):
        self.left = Node(data)

    def add_right(self,data):
        self.right = Node(data)


class BinTree:
    def __init__(self,data):
        self.root = Node(data)

def add_Node_Order(ele, node):
    if node.data <= ele:
        if node.left is None:
            node.add_left(ele)
        else:
            add_Node_Order(ele, node.left)
    else:
        if node.right is None:
            node.add_right(ele)
        else:
            add_Node_Order(ele, node.right)

def print_all_nodes(node):
    if node.left is not None:
        print(node.data)
        print_all_nodes(node.left)
    if node.right is not None:
        print(node.data)
        print_all_nodes(node.right)


def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)


# Print nodes at a given level
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)

#TODO link left node as prev node to make doubly linked list
def flatten(root):
    if root != None or root.left != None or root.right != None:
        return

    tmp_node = root.right
    root.right = root.left
    root.left = None

    move_node = root.right

    while(move_node.right != None):
        move_node = move_node.right

    move_node.right = tmp_node

    flatten(root.right)


def inorder(root):
    # Base condition
    if (root == None):
        return

    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)


tree = BinTree(50)
x = 0
print(tree.root.data)
print()
print()
while x < 50:
    test = random.randint(0,101)
    add_Node_Order(test, tree.root)
    x+=1

inorder(tree.root)
flatten(tree.root)
inorder(tree.root)







